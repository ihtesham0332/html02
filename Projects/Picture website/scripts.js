const pic = document.querySelectorAll(".slider");
var counter = 0;

pic.forEach((slider, index) => {
    slider.style.left = `${index * 100}%`;
});

const Next = () => {
    counter++;
    if (counter >= pic.length) {
        counter = 0;
    }
    slideimg();
};

const Previous = () => {
    counter--;
    if (counter < 0) {
        counter = pic.length - 1;
    }
    slideimg();
};

const slideimg = () => {
    pic.forEach((slider) => {
        slider.style.transform = `translateX(-${counter * 100}%)`;
    });
};