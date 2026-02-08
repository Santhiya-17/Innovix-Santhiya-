document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("careerForm");
    const resultBox = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // prevent reload

        const formData = new FormData(form);

        try {
            const response = await fetch("/analyze", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            resultBox.innerHTML = `
                <h3>Suggested Career Domain:</h3>
                <h2>${data.domain}</h2>
                <div class="roadmap-box">${data.roadmap}</div>
            `;
        } catch (err) {
            resultBox.innerHTML = `<p style="color:red;">Error fetching results. Please try again.</p>`;
            console.error(err);
        }
    });
});


