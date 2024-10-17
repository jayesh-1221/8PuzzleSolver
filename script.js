const puzzleContainer = document.getElementById("puzzle-container");
const shuffleButton = document.getElementById("shuffle-button");

// Initial puzzle state
let puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0];

// Function to create the puzzle grid
function createPuzzle() {
    puzzleContainer.innerHTML = ""; // Clear existing tiles
    puzzle.forEach((number, index) => {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        if (number === 0) {
            tile.classList.add("empty");
        } else {
            tile.textContent = number;
            tile.addEventListener("click", () => moveTile(index));
        }
        puzzleContainer.appendChild(tile);
    });
}

// Function to find the index of the empty space (0)
function findEmptySpace() {
    return puzzle.indexOf(0);
}

// Function to check if the move is valid
function isValidMove(index) {
    const emptyIndex = findEmptySpace();
    const validMoves = [
        emptyIndex - 1, // left
        emptyIndex + 1, // right
        emptyIndex - 3, // up
        emptyIndex + 3  // down
    ];
    return validMoves.includes(index);
}

// Function to swap tiles
function swapTiles(index1, index2) {
    [puzzle[index1], puzzle[index2]] = [puzzle[index2], puzzle[index1]];
}

// Function to move the tile
function moveTile(index) {
    if (isValidMove(index)) {
        const emptyIndex = findEmptySpace();
        swapTiles(index, emptyIndex);
        createPuzzle();

        // Check if solved
        if (isSolved()) {
            alert("Congratulations! You solved the puzzle.");
        }
    }
}

// Function to check if the puzzle is solved
function isSolved() {
    return puzzle.every((value, index) => value === (index + 1) % 9);
}

// Function to shuffle the puzzle
function shufflePuzzle() {
    for (let i = puzzle.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        if (isValidMove(j)) {
            swapTiles(i, j);
        }
    }
    createPuzzle();
}

// Event listener for the shuffle button
shuffleButton.addEventListener("click", shufflePuzzle);

// Initialize the puzzle
createPuzzle();
