    console.log("fcdvdvddsvsvd");
    

    fetch("sample-data.JSON")
    .then(response => response.json())
    .then(data =>
        console.log(data.category))


const cardDataFeeder = (data) => 
`
<div class="card-main-inner-card">
<img
src="index.jpg"
alt="card-show-image"
class="card-image"
/>

<div class="card-text-section">
    <div class="name-and-description">
        
          <div class="name_dist_rate">
            <h4 class="name_dist_rate_title">${data["name"]}</h4>
            <div class="dist_rate">
              <span class="dist"
                ><i class="fa fa-map-marker" aria-hidden="true"></i>&ensp;${data["distance"]}
              </span>
              <span class="rating"
                >${data["ratings"]}&ensp;<i class="fa fa-star" aria-hidden="true"></i
              ></span>
            </div>
          
            </div>
        <div class="address">
        ${data["address"]}
        </div>
        <div class="time">Timings: ${data["timings"]}</div>
        
        <div class="contact_dir_amt">
          <button class="contact">CONTACT US</button>
          <button class="dir">DIRECTION</button>
        </div>
    
</div>
</div>
</div>
`;

for (let i = 0; i < data.length; i++) {
    allHTML += cardDataFeeder(data[i]);
  }