function setSliderValue(evt) {
    evt.preventDefault();
    let num_words = "2.0";
    $.ajax({
        url: "/set_num_words.json",
        method: "POST",
        data: {num_words: num_words},
        // success: showJoke,
    });
}

$(window).on("load", setSliderValue);


function updateNumWords(evt) {
    evt.preventDefault();
    let num_words = this.value;
    $.ajax({
        url: "/set_num_words.json",
        method: "POST",
        data: {num_words: num_words},
        // success: showJoke,
    });
}

$("#slider-num-words").on("change", updateNumWords);


function showRandomJoke(response) {
    let joke_html_string = '<div id="joke-div-1"><p class="joke"><b>Click me -->>&nbsp;&nbsp;&nbsp; </b>';
    let word_counter = 1;
    if ("jokes" in localStorage) {
        let prev_jokes = JSON.parse(localStorage.getItem("jokes"));
        prev_jokes.push(response);
        localStorage.setItem("jokes", JSON.stringify(prev_jokes));
    } else {
        localStorage.setItem("jokes", JSON.stringify([response]));
    }
    let response_split = response.split(" ");
    for (let word of response_split) {
        joke_html_string += `<span class="joke-text joke-1" id="word-${word_counter}" value="${word}">${word} </span>`;
        word_counter += 1;
    }
    joke_html_string += '</p></div><div id="joke-div-2"></div><div id="joke-div-3"></div><div id="joke-div-4"></div><div id="joke-div-5"></div>';
    $("#outer-jokes-div").html(joke_html_string);
}

function getRandomJoke(evt) {
    evt.preventDefault();
    $.ajax({
        url: "/get_random_joke.json",
        success: showRandomJoke,
    });
}

$("#home-main-joke-btn").on("click", getRandomJoke);


function showStoredJokes(evt) {
    evt.preventDefault();
    let joke_html_string = "";
    if ("jokes" in localStorage) {
        let jokes = JSON.parse(localStorage.getItem("jokes"));
        for (let joke of jokes) {
            if (typeof joke === "string") {
                joke_html_string += `<div type="text" class="prev-joke-text" id="prev-joke-text">${joke} </div><br>`;
            }
        }
    } else {
        alert("There are no saved jokes");
    }

    $("#outer-jokes-div").html(joke_html_string);
}

$("#prev-joke-btn").on("click", showStoredJokes);


function showJoke(response) {
    let joke_html_string = '<p class="joke">';
    let word_counter = 1;
    let response_joke = response["joke"];
    let index_marker = response["index_marker"];
    let prev_class = response["joke_class"];
    let response_split = response_joke.split(" ");
    let prev_class_split = prev_class.split("-");
    let next_class = Number(prev_class_split[2]) + 1;
    if ("jokes" in localStorage) {
        let prev_jokes = JSON.parse(localStorage.getItem("jokes"));
        prev_jokes.push(response_joke);
        localStorage.setItem("jokes", JSON.stringify(prev_jokes));
    } else {
        localStorage.setItem("jokes", JSON.stringify([response_joke]));
    }
    if (next_class === 2) {
        joke_html_string += "<b>Click me too -->>&nbsp;&nbsp;&nbsp; </b>";
    } else if (next_class === 3) {
        joke_html_string += "<b>Me too -->>&nbsp;&nbsp;&nbsp; </b>";
    } else if (next_class === 4) {
        joke_html_string += "<b>And me -->>&nbsp;&nbsp;&nbsp; </b>";
    } else if (next_class === 5) {
        joke_html_string += "<b>But not me --||&nbsp;&nbsp;&nbsp; </b>";
    }
    for (let word of response_split) {
        if (word_counter === Number(index_marker)) {
            joke_html_string += `<span class="red joke-text joke-${next_class}" id="word-${word_counter}" value="${word}">${word} </span>`;
        } else {
            joke_html_string += `<span class="joke-text joke-${next_class}" id="word-${word_counter}" value="${word}">${word} </span>`;
        }
        word_counter += 1;
    }
    joke_html_string += '</p>';
    $(`#joke-div-${next_class}`).html(joke_html_string);
}

function setRed(evt) {
    evt.preventDefault();
    $(this).css("color", "red");
    $(this).css("font-weight", "bold");
}

function getJoke(evt) {
    evt.preventDefault();
    let user_input = $(this).attr("value");
    let joke_class = $(this).attr("class");
    $.ajax({
        url: "/get_not_random_joke.json",
        method: "POST",
        data: {
            user_input: user_input,
            joke_class: joke_class
        },
        success: showJoke,
    });
}

$("#outer-jokes-div").on("click", ".joke-1", getJoke);
$("#outer-jokes-div").on("click", ".joke-1", setRed);
$("#outer-jokes-div").on("click", ".joke-2", getJoke);
$("#outer-jokes-div").on("click", ".joke-2", setRed);
$("#outer-jokes-div").on("click", ".joke-3", getJoke);
$("#outer-jokes-div").on("click", ".joke-3", setRed);
$("#outer-jokes-div").on("click", ".joke-4", getJoke);
$("#outer-jokes-div").on("click", ".joke-4", setRed);

