let map = `#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
#########################
###########@#############
#########################
#########################
#########################
`
const size = 32;
let cvs = document.getElementById("canvas");
let ctx = cvs.getContext("2d");

let player = new Image();
let brick = new Image();
let bg = new Image();


player.src = "../images/playerW.png";
brick.src = "../images/bricks.png"
bg.src = "../images/bg.png";
document.addEventListener('keydown', function (event) {
    if (event.code == 'KeyW') {
        user.move(0, -1);
        player.src = "../images/playerW.png";
    }
    if (event.code == 'KeyA') {
        user.move(-1, 0);
        player.src = "../images/playerA.png";
    }
    if (event.code == 'KeyS') {
        user.move(0, 1);
        player.src = "../images/playerS.png";
    }
    if (event.code == 'KeyD') {
        user.move(1, 0);
        player.src = "../images/playerD.png";
    }
});

class tank {

    constructor(Xpos, Ypos, health, speed, sprite, direction) {
        this._Xpos = Xpos;
        this._Ypos = Ypos;
        this._health = health;
        this._speed = speed;
        this._sprite = sprite;
        this.direction = direction;
    }
    getXpos() {
        return this._Xpos;
    }
    getYpos() {
        return this._Ypos;
    }
    getSpeed() {
        return this._speed;
    }
    setpos(newXpos, newYpos) {
        this._Xpos = newXpos;
        this._Ypos = newYpos;

    }
    move(moveX, moveY) {
        this.setpos(this.getXpos() + moveX * this.getSpeed(), this.getYpos() + moveY * this.getSpeed());
        if (moveY < 0)
            this.direction = "w";
        if (moveX < 0)
            this.direction = "a";
        if (moveY > 0)
            this.direction = "s";
        if (moveX > 0)
            this.direction = "d";
    }
}
let user = new tank(400 - 16, 800 - 32, 5, 5, player, "w");
function draw() {
    ctx.drawImage(bg, 0, 0);
    ctx.drawImage(user._sprite, user.getXpos(), user.getYpos(), 32, 32);
    let i = 0, j = 0;
    for (let  char of map) {
        if (char == "@") {
            ctx.drawImage(brick, i * size, j * size);
        }
        i++;
        if (i % 26 == 0) {
            j++;
            i = 0;
        }
    }
    for (let col = 0; col < 26; col++)
        for (let row = 0; row < 26; row++)
            if (map[col * 26 + row] == "@") {
                if ((col * 32 + 32 > user.getYpos() && row * 32 + 31 > user.getXpos() && col * 32 < user.getYpos() && row * 32 + 1 < user.getXpos()) ||
                    (col * 32 + 32 > user.getYpos() && row * 32 + 32 > user.getXpos() + 32 &&
                        col * 32 < user.getYpos() && row * 32 < user.getXpos() + 32))
                    user.move(0, 1);
                if (row * 32 - 32 < user.getXpos() && col * 32 - 32 < user.getYpos() && col * 32 > user.getYpos() && row * 32 > user.getXpos() )
                    user.move(-1, 0);
            }
    requestAnimationFrame(draw);
}
bg.onload = draw;
draw();
