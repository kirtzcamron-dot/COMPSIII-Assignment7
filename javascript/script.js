const fruits = ["apple", "banana", "orange", "strawberry"];
const vegetables = ["carrot", "broccoli", "spinach", "pepper"];
const junkFood = ["chips", "candy", "soda", "pizza"];


console.log("Fruits list:");
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

function showFood(category) {
    console.log("Food category:", category);
}


showFood("Fruits");
showFood("Vegetables");

console.log("Healthy foods:");

for (let i = 0; i < fruits.length; i++) {
    if (fruits[i] !== "banana") {  
        console.log(fruits[i]);
    }
}

if (fruits.length > vegetables.length) {
    console.log("More fruits than vegetables");
} else if (fruits.length < vegetables.length) {
    console.log("More vegetables than fruits");
} else {
    console.log("Same number of fruits and vegetables");
}

let searchItem = "pizza";

if (junkFood.includes(searchItem)) {
    console.log(searchItem + " is in the junk food list");
} else {
    console.log(searchItem + " is not in the list");
}
✅ What This
