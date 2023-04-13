
let MyDate = new Date();
let MyDateString;

MyDate.setDate(MyDate.getDate());

day = MyDate.getFullYear() + "-" + ('0' + (MyDate.getMonth()+1)).slice(-2) + "-" + ('0' + MyDate.getDate()).slice(-2);

     console.log(day);
     
const settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://api-football-beta.p.rapidapi.com/fixtures?date=" + day,
    "method": "GET",
    "headers": {
        "X-RapidAPI-Key": "7d134d7b75msh7bd2fd08ebc6fd9p18362djsncaea62c7b8c8",
        "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
    }
};

$.ajax(settings).done(function (response) {
    console.log(response['response']['0']);
    let responses = response['response'];

    buildTable(responses);
});

function buildTable(data) {
    const table = document.getElementById("table");

    for (var i = 0; i < 21; i++ ) {
        var row = `
            <div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="0.3s" style=" border-bottom-left-radius: 25px">
                <div class="causes-item d-flex flex-column bg-white border-top border-5 border-primary rounded-top overflow-hidden h-100">
                    <div class="text-center p-4 pt-0">
                        <div class="d-inline-block bg-primary text-white rounded-bottom fs-5 pb-1 px-3 mb-4">
                            <small>【${data[i].league.name}】</small>
                        </div>
                        <h5 class="mb-3"> <div class="d-flex justify-content-between">
                            <img src="${data[i].teams.home.logo}" style="height: 50px; width: 50px; border-radius:50%;" alt="" srcset="">
                            <p class="text-dark"> <small class="text-body">Vs</small></p>
                            <img src="${data[i].teams.away.logo}" style="height: 50px; width: 50px; border-radius:50%;" alt="" srcset="">
                        </div></h5>
                        <p>${data[i].fixture.date}</p>
                        <div class="causes-progress bg-light p-3 pt-2">
                            <div class="d-flex text-center">
                                <p class="text-dark text-center"> Trading Volume</p>
                                <!-- <p class="text-dark">$9,542 <small class="text-body">Raised</small></p> -->
                            </div>
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100">
                                    <span>2360K</span>
                                </div>
                            </div>
                            <div class="col-12 mt-4">
                                <div class="btn-group d-flex justify-content-around" style="border-radius: 25px;">
                                    <input type="radio" class="btn-check" name="btnradio" id="btnradio1" checked style="border-radius: 25px;">
                                    <label class="btn btn-light py-3" for="btnradio1" style="background-color: #FF6F0F; color: #fff;">Hot Score</label>
    
                                    <input type="radio" class="btn-check " name="btnradio" id="btnradio2">
                                    <label class="btn btn-light py-3" for="btnradio2"> ${data[i].goals.home} - ${data[i].goals.away}</label>
    
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        `
        table.innerHTML += row;
    }
}







// matchresultAPI
