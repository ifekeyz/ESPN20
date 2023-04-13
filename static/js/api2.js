
let MyDate1 = new Date();
let MyDateString1;

MyDate1.setDate(MyDate1.getDate());

day =
    MyDate1.getFullYear() +
    "-" +
    ("0" + (MyDate1.getMonth() + 1)).slice(-2) +
    "-" +
    ("0" + MyDate1.getDate()).slice(-2);

console.log(day);

const settings1 = {
    async: true,
    crossDomain: true,
    url: "https://v3.football.api-sports.io/fixtures?date=" + day,
    method: "GET",
    headers: {
        "X-RapidAPI-Key": "0a731fadc8d211d66a7453f23860f640",
        "X-RapidAPI-Host": "v3.football.api-sports.io",
    },
};

$.ajax(settings1).done(function (response) {
    console.log(response["response"]["0"]);
    let responses = response["response"];

    buildTable(responses);
});

function buildTable(data) {
    const table = document.getElementById("matchresult");

    for (var i = 0; i < 32; i++) {
        var row = `
                    <tr>
                        <th scope="row">${data[i].fixture.status.long}</th>
                        <td>${data[i].fixture.time}</td>
                        <td>${data[i].league.name} <br> ${data[i].league.round} </td>
                        <td>${data[i].teams.home.name}</td>
                        <td>${data[i].teams.away.name}</td>
                        <td>${data[i].goals.home} - ${data[i].goals.away}</td>
                        <td>${data[i].score.halftime.home} - ${data[i].score.halftime.away}</td>
                    </tr>
                `;
        table.innerHTML += row;
    }
}
