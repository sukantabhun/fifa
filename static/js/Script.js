function jumpToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
}

document.addEventListener("DOMContentLoaded", function () {
    const animateText = (element) => {
        const text = element.textContent;
        element.textContent = "";

        for (let i = 0; i < text.length; i++) {
            setTimeout(() => {
                element.textContent += text[i];
            }, i * 50);
        }
    };

    const elementsToAnimate = document.querySelectorAll(".fade-in");
    elementsToAnimate.forEach(animateText);
});
document.addEventListener("DOMContentLoaded", function () {
    const animateText = (element) => {
        const text = element.textContent;
        element.textContent = "";

        for (let i = 0; i < text.length; i++) {
            setTimeout(() => {
                element.textContent += text[i];
            }, i * 25); 
        }
    };

    const textToAnimate = document.getElementById("animated-text");
    animateText(textToAnimate);
});
//dash_board
// leaderboard/static/js/script.js

document.addEventListener("DOMContentLoaded", function () {
    const worldCupWinners = {
      "Brazil": 6,
      "Germany": 4,
      "Italy": 4,
      "Uruguay": 2,
      "Argentina": 2,
      "France": 2,
      "England": 1,
      "Spain": 1,
      "West Germany": 3,
    };
  
    const leaderboardTable = document.getElementById("leaderboard-table");
    const leaderboardBody = document.getElementById("leaderboard-body");
  
    Object.entries(worldCupWinners).forEach(([team, wins], index) => {
      const row = leaderboardBody.insertRow();
      const positionCell = row.insertCell(0);
      const teamCell = row.insertCell(1);
      const winsCell = row.insertCell(2);
  
      positionCell.textContent = index + 1;
      teamCell.textContent = team;
      winsCell.textContent = wins;
    });
  
    leaderboardTable.style.display = "table"; // Show leaderboard table
  });
  