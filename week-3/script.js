fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){

        console.log(data);

        for (i=0; i<2; i++) {

            let container = document.querySelectorAll(".box")[0+i];
            let title = document.createElement("a");
            let imgArray = data.result.results[i].file.split('http')[1]
            title.textContent =data.result.results[i].stitle;
            let img = document.createElement("img");       
            img.setAttribute("src", 'http'+imgArray);            
            container.append(img);
            container.append(title);
          }

        for (i=2 ; i<10 ; i++){

            let container_two = document.querySelectorAll(".box")[0+i];
            let title = document.createElement("p");
            let imgArray = data.result.results[i].file.split('http')[1]
            title.textContent =data.result.results[i].stitle;
            let img = document.createElement("img");       
            img.setAttribute("src", 'http'+imgArray);            
            container_two.append(img);
            container_two.append(title);

        }

    })

