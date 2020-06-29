$(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Number of infected packets",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 0, 0)',
                data: [],
                fill: false,
            },{
                label: "Number of packets",
                backgroundColor: 'rgb(99, 255, 132)',
                borderColor: 'rgb(0, 255, 0)',
                data: [],
                fill: false,
            },{
                label: "Pourcentage of packets",
                backgroundColor: 'rgb(132, 99, 255)',
                borderColor: 'rgb(0, 0, 255)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Evolution of packets on the Network'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };

    const context = document.getElementById('canvas').getContext('2d');

    const lineChart = new Chart(context, config);

    const source = new EventSource("/chart-data");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config.data.labels.length === 20) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
            config.data.datasets[1].data.shift();
            config.data.datasets[2].data.shift();
        }
        config.data.labels.push(data.time);
        config.data.datasets[0].data.push(data.value[0]);
        config.data.datasets[1].data.push(data.value[1]);
        if (data.value[1] == 0)
            data.value[1] = 1
        config.data.datasets[2].data.push((data.value[0] / data.value[1]) * 100);
        lineChart.update();
        if (((data.value[0] / data.value[1]) * 100 > data.value[2]) && data.value[1] > 100)
            alert("MORE THAN " + data.value[2] + "% OF INFECTED PACKETS DETECTED (" + (data.value[0] / data.value[1]) * 100 + ")");
    }
});