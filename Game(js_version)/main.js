let map = `#########################
#########################
###@@@@@@@@##@@@@@@@@@###
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@###############@####
####@@@###########@@@####
######@###@@@@@###@######
######@###########@######
######@###########@######
#########################
#########################
#########################
@@@@@@@@@@#####@@@@@@@@@@
#########################
#########################
#########################
`
const size = 32;
let cvs = document.getElementById("canvas");
let ctx = cvs.getContext("2d");

let player = new Image();
let brick = new Image();
let bulletW = new Image();
let bulletA = new Image();
let bulletS = new Image();
let bulletD = new Image();
let bg = new Image();

String.prototype.replaceAt = function (index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

player.src = "../images/playerW.png";
brick.src = "../images/bricks.png";
bulletW.src = "../images/fireW.png";
bulletA.src = "../images/fireA.png";
bulletS.src = "../images/fireS.png";
bulletD.src = "../images/fireD.png";
bg.src = "../images/bg.png";
let animationPlayermodel = false;
document.addEventListener('keydown', function (event) {
    if (event.code == 'KeyW') {
        user.move(0, -1);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerW.png";
        else
            player.src = "../images/playerW1.png";
    }
    if (event.code == 'KeyA') {
        user.move(-1, 0);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerA.png";
        else
            player.src = "../images/playerA1.png";
    }
    if (event.code == 'KeyS') {
        user.move(0, 1);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerS.png";
        else
            player.src = "../images/playerS1.png";
    }
    if (event.code == 'KeyD') {
        user.move(1, 0);
        animationPlayermodel = !animationPlayermodel;
        if (animationPlayermodel)
            player.src = "../images/playerD.png";
        else
            player.src = "../images/playerD1.png";
    }
    if (event.code == 'Space') {
        user.fire(bullets);
    }
});
class projectile {
    constructor(Xpos, Ypos, direction, speed, sprite) {
        this._Xpos = Xpos;
        this._Ypos = Ypos;
        this._direction = direction;
        this._speed = speed;
        this._sprite = sprite;
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
            this._direction = "w";
        if (moveX < 0)
            this._direction = "a";
        if (moveY > 0)
            this._direction = "s";
        if (moveX > 0)
            this._direction = "d";
    }
    getDirection() {
        return this._direction;
        }
    fly(map) {
        if (this._direction == "w") {
            this._sprite = bulletW;
            this.move(0, -1);
        }
        if (this._direction == "a") {
            this._sprite = bulletA;
            this.move(-1, 0);
        }
        if (this._direction == "s") {
            this._sprite = bulletS;
            this.move(0, 1);
        }
        if (this._direction == "d") {
            this._sprite = bulletD;
            this.move(1, 0);
        }
        /*for (let col = 0; col < 26; col++)
            for (let row = 0; row < 26; row++)
                if (map[col * 26 + row] == "@") {
                    if (col * 32 + 32 > this.getYpos() && row * 32 + 32 > this.getXpos() && col * 32 < this.getYpos() && row * 32 - 32 < this.getXpos())
                        return map.replaceAt(col * 26 + row, "#");
                }*/
    }

}

class tank {
    constructor(Xpos, Ypos, health, speed, sprite, direction) {
        this._Xpos = Xpos;
        this._Ypos = Ypos;
        this._health = health;
        this._speed = speed;
        this._sprite = sprite;
        this._direction = direction;
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
            this._direction = "w";
        if (moveX < 0)
            this._direction = "a";
        if (moveY > 0)
            this._direction = "s";
        if (moveX > 0)
            this._direction = "d";
    }
    getDirection() {
        return this._direction;
    }
    fire(newbullets) {
        newbullets.push(new projectile(user.getXpos()+12, user.getYpos()+12, user.getDirection(), 3, bulletW));
    }
}
let user = new tank(400 - 16, 800 - 32, 5, 8, player, "w");
let bullets = new Array();
function draw() {
    ctx.drawImage(bg, 0, 0);
    for (let bull of bullets) {
        ctx.drawImage(bull._sprite, bull.getXpos(), bull.getYpos());
        bull.fly(map);
    }
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
    map = map.replaceAt(2 * 26 + 2, "@");
    if (user.getYpos() > 800 - 32)
        user.setpos(user.getXpos(), user.getYpos() - user.getSpeed());
    if (user.getYpos() < 0)
        user.setpos(user.getXpos(), user.getYpos() + user.getSpeed());
    if (user.getXpos() > 800 - 32)
        user.setpos(user.getXpos() - user.getSpeed(), user.getYpos());
    if (user.getXpos() < 0)
        user.setpos(user.getXpos() + user.getSpeed(), user.getYpos());
    for (let col = 0; col < 26; col++)
        for (let row = 0; row < 26; row++)
            if (map[col * 26 + row] == "@") {
                if (user.getDirection() == "w")
                    if (col * 32 + 32 > user.getYpos() && row * 32 + 32 > user.getXpos() && col * 32 < user.getYpos() && row * 32 - 32 < user.getXpos())
                        user.setpos(user.getXpos(), user.getYpos() + user.getSpeed());
                if (user.getDirection() == "d")
                    if (row * 32 - 32 < user.getXpos() && col * 32 - 32 < user.getYpos() && col * 32+32> user.getYpos() && row * 32 > user.getXpos())
                        user.setpos(user.getXpos() - user.getSpeed(), user.getYpos());
                if (user.getDirection() == "a")
                    if (row * 32 + 32 > user.getXpos() && col * 32 - 32 < user.getYpos() && col * 32 + 32 > user.getYpos() && row * 32 < user.getXpos())
                        user.setpos(user.getXpos() + user.getSpeed(), user.getYpos());
                if (user.getDirection() == "s")
                    if (col * 32 - 32 < user.getYpos() && row * 32 + 32 > user.getXpos() && row * 32 - 32 < user.getXpos() && col * 32 > user.getYpos())
                        user.setpos(user.getXpos(), user.getYpos() - user.getSpeed());
            }
    requestAnimationFrame(draw);
}
bg.onload = draw;
draw();
