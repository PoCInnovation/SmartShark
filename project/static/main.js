const ddos_config = {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Number of infected packets",
        backgroundColor: "rgb(255, 99, 132)",
        borderColor: "rgb(255, 0, 0)",
        data: [],
        fill: false,
      },
      {
        label: "Number of packets",
        backgroundColor: "rgb(99, 255, 132)",
        borderColor: "rgb(0, 255, 0)",
        data: [],
        fill: false,
      },
      {
        label: "Number of SPY packets",
        backgroundColor: "rgb(132, 99, 255)",
        borderColor: "rgb(0, 0, 255)",
        data: [],
        fill: false,
      },
    ],
  },
  options: {
    responsive: true,
    title: {
      display: true,
      text: "Packet Trafic",
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Time",
          },
        },
      ],
      yAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Value",
          },
        },
      ],
    },
  },
};

const ddos_percent_config = {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Percent of infected packets",
        backgroundColor: "rgb(255, 99, 132)",
        borderColor: "rgb(255, 99, 132)",
        data: [],
        fill: false,
      },
      {
        label: "Percent of spy packets",
        backgroundColor: "rgb(132, 99, 255)",
        borderColor: "rgb(132, 99, 255)",
        data: [],
        fill: false,
      },
    ],
  },
  options: {
    responsive: true,
    title: {
      display: true,
      text: "Percent of Infected Packets",
    },
    tooltips: {
      mode: "index",
      intersect: false,
    },
    hover: {
      mode: "nearest",
      intersect: true,
    },
    scales: {
      xAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Time",
          },
        },
      ],
      yAxes: [
        {
          display: true,
          scaleLabel: {
            display: true,
            labelString: "Value",
          },
        },
      ],
    },
  },
};

$(document).ready(function () {
  const ddos_context = document.getElementById("ddos_context").getContext("2d");
  const ddos_lineChart = new Chart(ddos_context, ddos_config);

  const ddos_percent_context = document
    .getElementById("percent")
    .getContext("2d");
  const ddos_percent_lineChart = new Chart(
    ddos_percent_context,
    ddos_percent_config
  );

  const source = new EventSource("/chart-data");

  source.onmessage = function (event) {
    const data = JSON.parse(event.data);

    if (ddos_config.data.labels.length === 20) {
      ddos_config.data.labels.shift();
      ddos_config.data.datasets[0].data.shift();
      ddos_config.data.datasets[1].data.shift();
      ddos_config.data.datasets[2].data.shift();
    }
    ddos_config.data.labels.push(data.time);
    ddos_config.data.datasets[0].data.push(data.value[0]);
    ddos_config.data.datasets[1].data.push(data.value[1]);
    ddos_config.data.datasets[2].data.push(data.value[4]);
    ddos_lineChart.update();

    if (ddos_percent_config.data.labels.length === 20) {
      ddos_percent_config.data.labels.shift();
      ddos_percent_config.data.datasets[0].data.shift();
      ddos_percent_config.data.datasets[1].data.shift();
    }
    ddos_percent_config.data.labels.push(data.time);
    if (data.value[1] == 0) data.value[1] = 1;
    ddos_percent_config.data.datasets[0].data.push(
      (data.value[0] / data.value[1]) * 100
    );
    ddos_percent_config.data.datasets[1].data.push(
      (data.value[4] / data.value[1]) * 100
    );
    ddos_percent_lineChart.update();
    if (
      (data.value[0] / data.value[1]) * 100 > data.value[2] &&
      data.value[1] > 100
    )
      alert(
        "MORE THAN " +
          data.value[2] +
          "% OF INFECTED PACKETS DETECTED (" +
          (data.value[0] / data.value[1]) * 100 +
          ")"
      );
  };
  $(".input3 form").on("submit", function (event) {
    $.ajax({
      data: { cmd: $("#cmd_3").val() },
      type: "POST",
      url: "/",
    });
    event.preventDefault();
  });

  $(".input1 form").on("submit", function (event) {
    $.ajax({
      data: { cmd: $("#cmd_1").val() },
      type: "POST",
      url: "/",
    });
    event.preventDefault();
  });

  $(".input2 form").on("submit", function (event) {
    $.ajax({
      data: { cmd: $("#cmd_2").val() },
      type: "POST",
      url: "/",
    });
    event.preventDefault();
  });

  $(".input4 form").on("submit", function (event) {
    $.ajax({
      data: { cmd: $("#cmd_4").val() },
      type: "POST",
      url: "/",
    });
    event.preventDefault();
  });

  $(".input5 form").on("submit", function (event) {
    $.ajax({
      data: { cmd: $("#cmd_5").val() },
      type: "POST",
      url: "/",
    });
    event.preventDefault();
  });
});
