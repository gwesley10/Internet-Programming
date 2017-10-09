var util = {

    write: function (x) {
        var console = document.getElementById("my-console");
        if (!console) {
            console = document.createElement('div');
            console.setAttribute("id", "my-console");
            document.getElementsByTagName('body')[0].appendChild(console);
        }

        for (var i = 0; i < arguments.length; i++) {
            //console.appendChild(document.createTextNode(arguments[i]));
            console.innerHTML += arguments[i];
        }

    },

    newLine: function () {
        this.write("<br/>");
    },

    par: function (x) {
        this.write("<p>" + x + "</p>");
    },

    rule: function () {
        this.write("<hr/>");
    },


    writeln: function (x) {
        this.write(x);
        this.newLine();
    },
}