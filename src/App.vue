<script setup>
import { RouterView } from 'vue-router'
import AllInfusions from '@/assets/generated_data_unique_with_time.json'
import { provide, ref, watch, onMounted } from 'vue'
import { ToggleGroupItem, ToggleGroupRoot, Toggle } from 'radix-vue'
import InfusionButtons from '@/components/InfusionButtons.vue'
import { Icon } from '@iconify/vue'
import { selectedButtoneStore } from '@/stores/selectedButtonStore.js'

let currentInfusions = AllInfusions

const initializeImageMapPro = () => {
  if (window.ImageMapPro) {
    window.ImageMapPro.init('#image-map-pro', {"id":"a7efa49f-86a0-42aa-99c9-f329941c546e","general":{"name":"diakonessenhuis"},"tooltips":{"enable_tooltips":false,"tooltip_animation":"fade","fullscreen_tooltips":"none"},"object_list":{"group_by_artboard":true,"show_groups":false,"show_only_objects_from_active_artboard":true,"hide_static_objects":false},"artboards":[{"title":"overview","background_type":"image","image_url":"https://i.postimg.cc/N0rGCk8W/voorkant.png","width":1132,"height":800,"children":[{"id":"6cfcf5f5-f78a-420d-8646-250118646f79","title":"main floor","type":"poly","x":15.017667844522965,"y":60.259712514414495,"width":84.98233215547704,"height":10.296224645227507,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"actions":{"click":"change-artboard","artboard":"8c389e81-ef8c-4e71-81eb-fb76f4fc7fc4"},"x_image_background":15.061965511038952,"y_image_background":62.782643540587955,"points":[{"x":0.05197505197505198,"y":29.365079365079367},{"x":21.361746361746363,"y":11.11111111111111},{"x":59.1995841995842,"y":21.428571428571427},{"x":99.7920997920998,"y":0},{"x":100,"y":100},{"x":46.517671517671516,"y":85.71428571428571},{"x":21.82952182952183,"y":93.65079365079364},{"x":0,"y":94.44444444444444}]},{"id":"fc0a1509-0979-4af5-9d84-6506324d3036","title":"1st floor","type":"poly","x":15.150176678445238,"y":51.94091980753084,"width":84.84982332155477,"height":11.182641342756185,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"actions":{"click":"change-artboard","artboard":"56ad6ec0-7b5f-40d7-ab66-3d34d9b6e1e1"},"x_image_background":15.061965511038952,"y_image_background":54.25928885860915,"points":[{"x":0,"y":100},{"x":0.052056220718375845,"y":42.68292682926829},{"x":21.395106715252474,"y":0},{"x":58.82352941176471,"y":51.21951219512195},{"x":100,"y":20.73170731707317},{"x":100,"y":73.17073170731707},{"x":59.08381051535658,"y":91.46341463414635},{"x":21.499219156689225,"y":82.92682926829268}]},{"id":"aa8dbfd8-0c7e-4b5b-a68a-817386a42fac","title":"2nd floor","type":"poly","x":14.97349823321553,"y":40.27050716830188,"width":85.02650176678446,"height":17.796764575971743,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"actions":{"click":"change-artboard","artboard":"4706f4ed-8fc7-468c-a816-625346569165"},"x_image_background":15.02173460835703,"y_image_background":42.24793959422162,"points":[{"x":0,"y":43.67816091954023},{"x":21.402597402597408,"y":0},{"x":59.27272727272728,"y":62.068965517241395},{"x":100,"y":35.24904214559386},{"x":99.84415564808972,"y":79.31036948478129},{"x":59.06493388853827,"y":100},{"x":21.55844155844156,"y":65.90038314176243},{"x":0.15584415584415484,"y":93.10344827586205}]},{"id":"ce98c9af-479b-4317-a1fd-6112fe32c0e6","title":"3rd floor","type":"poly","x":15.04685340945992,"y":29.657988885083096,"width":84.8648070345089,"height":21.559518555297068,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"tooltip_style":{"position":"left"},"tooltip_content":[{"type":"Heading","text":"3rd floor","heading":"h3","other":{"id":"","classes":"","css":""},"style":{"fontFamily":"sans-serif","fontSize":20.8,"lineHeight":"normal","color":"#ffffff","textAlign":"left"},"boxModel":{"width":"auto","height":"auto","margin":{"top":0,"bottom":0,"left":0,"right":0},"padding":{"top":10,"bottom":10,"left":10,"right":10}},"id":"9eab6afb-c094-428b-badc-c75e53733147"},{"type":"Paragraph","text":"click to see floorplan","other":{"id":"","classes":"","css":""},"style":{"fontFamily":"sans-serif","fontSize":14,"lineHeight":22,"color":"#ffffff","textAlign":"left"},"boxModel":{"width":"auto","height":"auto","margin":{"top":0,"bottom":0,"left":0,"right":0},"padding":{"top":10,"bottom":10,"left":10,"right":10}},"id":"951e6045-17b6-40b9-8f0e-4bff6fcd2821"}],"actions":{"click":"change-artboard","artboard":"9bacbd67-e914-422a-a9df-dd792e2a09ab"},"x_image_background":0.10600814549746025,"y_image_background":19.924999237060547,"points":[{"x":0.024221407100784874,"y":83.99200725911473},{"x":21.20641087830483,"y":48.03671254334297},{"x":33.11554615840455,"y":64.4864411143178},{"x":59.29572568664051,"y":100},{"x":100,"y":77.86089313506854},{"x":100,"y":43.10176513164577},{"x":59.42656676946251,"y":77.88980639806871},{"x":33.31948054349822,"y":24.979722357186883},{"x":21.312722440955095,"y":0},{"x":0,"y":50.81999515653474}]},{"id":"2623e32b-7ac8-4264-8669-ca8931ed7b3d","title":"4th floor","type":"poly","x":15.017667677814803,"y":19.75673642898597,"width":84.9823323221852,"height":26.59286660777386,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"actions":{"click":"change-artboard","artboard":"0f24d9ab-d895-488c-a0c2-b43ad6cc8520"},"x_image_background":14.97362628842411,"y_image_background":21.529606879810565,"points":[{"x":0.15592515561927964,"y":77.6923076923077},{"x":21.309771267968355,"y":37.69230769230769},{"x":59.35550923907281,"y":100},{"x":99.94802475195887,"y":72.56410256410255},{"x":100,"y":63.589789426837065},{"x":100,"y":47.17925616053616},{"x":72.86902272607715,"y":70.25641025641023},{"x":59.35550923907281,"y":80.25641025641026},{"x":21.413721371714537,"y":0},{"x":0,"y":51.53846153846153}]},{"id":"e023b989-092c-4174-b94a-d4ea85ef1126","title":"5th floor","type":"poly","x":14.752779579836572,"y":5.369327443227331,"width":65.32686712666336,"height":35.6617159893993,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#00d5ff","background_opacity":0.5421521087557842,"stroke_color":"#0033ff","stroke_width":4},"actions":{"click":"change-artboard","artboard":"8d9e9f65-bd45-4397-a55c-52a0f7a5f8a8"},"x_image_background":14.752779579836572,"y_image_background":5.369327443227331,"points":[{"x":0,"y":54.875717017208416},{"x":27.924268026805656,"y":0},{"x":72.2109206845006,"y":73.80491389586302},{"x":94.97466463606943,"y":56.008272731900746},{"x":100,"y":69.98086997053421},{"x":99.79714190693738,"y":75.1434034416826},{"x":99.80181786231903,"y":91.6419752190342},{"x":96.8897608578624,"y":93.49903850815556},{"x":95.06421512273303,"y":92.1606118546845},{"x":77.41715954162825,"y":100},{"x":28.329947465451745,"y":41.10898661567878},{"x":0.3380661988717387,"y":78.58508604206503}]}]},{"id":"8c389e81-ef8c-4e71-81eb-fb76f4fc7fc4","title":"main floor","background_type":"image","image_url":"https://i.postimg.cc/8zZKXGnF/Nieuwbouw-00-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"ea9b6dcc-fdb5-438c-871f-1d0b394fc2da","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}}]},{"id":"56ad6ec0-7b5f-40d7-ab66-3d34d9b6e1e1","title":"1st floor","background_type":"image","image_url":"https://i.postimg.cc/nrf09hMW/Nieuwbouw-01-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"ea43bbdd-9370-4e5b-915b-57691beac116","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}}]},{"id":"4706f4ed-8fc7-468c-a816-625346569165","title":"2nd floor","background_type":"image","image_url":"https://i.postimg.cc/1zTWPHSs/Nieuwbouw-02-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"f5d2f735-95b3-4585-a424-b301219a704a","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}},{"id":"21eac194-3a33-4fe9-9f7c-25c240892aea","title":"Poly","type":"poly","x":44.055510072741825,"y":1.563455581665039,"width":44.87632508833923,"height":26.3125,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":44.055510072741825,"y_image_background":1.563455581665039,"points":[{"x":36.56496062992126,"y":24.584323040380045},{"x":0,"y":24.82185273159145},{"x":0.09842519685039369,"y":5.344418052256532},{"x":6.200787401574804,"y":0},{"x":100,"y":0.23752969121140144},{"x":99.75393700787401,"y":23.990498812351543},{"x":97.29330708661418,"y":24.584323040380045},{"x":97.58858267716536,"y":52.13776722090261},{"x":38.976377952755904,"y":100},{"x":38.927165354330704,"y":77.90973871733968},{"x":42.91338582677165,"y":75.17814726840855},{"x":42.1751968503937,"y":68.646080760095},{"x":42.37204724409449,"y":68.17102137767222},{"x":41.338582677165356,"y":59.73871733966746},{"x":38.927165354330704,"y":61.75771971496437},{"x":39.0255905511811,"y":42.042755344418055},{"x":36.26968503937008,"y":42.63657957244655},{"x":36.17125984251969,"y":39.548693586698334},{"x":36.76181102362205,"y":39.311163895486935}]},{"id":"99f714ba-f69a-4796-b4f7-2f27d09900fa","title":"Poly","type":"poly","x":46.70568675118706,"y":8.063455581665039,"width":16.541519434628967,"height":35.1875,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":46.70568675118706,"y_image_background":8.063455581665039,"points":[{"x":8.277703604806408,"y":0.08880994671403197},{"x":8.144192256341789,"y":3.463587921847247},{"x":0,"y":3.5523978685612785},{"x":0,"y":13.232682060390763},{"x":2.67022696929239,"y":13.587921847246893},{"x":1.8691588785046727,"y":76.82060390763765},{"x":8.277703604806408,"y":76.64298401420959},{"x":8.277703604806408,"y":87.65541740674956},{"x":11.882510013351135,"y":87.83303730017762},{"x":11.615487316421897,"y":93.8721136767318},{"x":22.029372496662216,"y":93.78330373001776},{"x":21.762349799732977,"y":97.7797513321492},{"x":36.315086782376504,"y":98.13499111900533},{"x":36.315086782376504,"y":87.92184724689164},{"x":81.70894526034714,"y":88.36589698046181},{"x":82.37650200267022,"y":100},{"x":89.31909212283044,"y":99.82238010657194},{"x":89.18558077436583,"y":39.96447602131439},{"x":100,"y":37.56660746003552},{"x":98.13084112149532,"y":33.57015985790409},{"x":98.6648865153538,"y":32.859680284191825},{"x":95.72763684913218,"y":26.376554174067497},{"x":89.18558077436583,"y":28.24156305506217},{"x":89.31909212283044,"y":12.788632326820604},{"x":82.2429906542056,"y":13.410301953818829},{"x":81.44192256341789,"y":11.101243339253998},{"x":83.71161548731642,"y":11.101243339253998},{"x":83.31108144192257,"y":0}]},{"id":"b5a10edc-1743-4b91-bfb8-d9af6c7e055d","title":"Poly","type":"poly","x":31.577594878395537,"y":35.06345558166504,"width":18.794169611307424,"height":8.90625,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":31.577594878395537,"y_image_background":35.06345558166504,"points":[{"x":0,"y":0.7017543859649122},{"x":0.35252643948296125,"y":99.29824561403508},{"x":11.750881316098708,"y":99.29824561403508},{"x":12.45593419506463,"y":89.47368421052632},{"x":15.276145710928319,"y":89.82456140350877},{"x":15.158636897767334,"y":98.94736842105263},{"x":65.21739130434783,"y":100},{"x":65.4524089306698,"y":89.12280701754386},{"x":70.0352526439483,"y":89.47368421052632},{"x":70.0352526439483,"y":99.29824561403508},{"x":100,"y":99.29824561403508},{"x":99.41245593419507,"y":67.71929824561404},{"x":90.36427732079906,"y":68.0701754385965},{"x":90.48178613396006,"y":44.21052631578947},{"x":87.3090481786134,"y":44.91228070175438},{"x":87.54406580493537,"y":0}]},{"id":"e21dbfca-8199-42e8-94ae-482796f05094","title":"Poly","type":"poly","x":61.39208251090438,"y":33.68845558166504,"width":8.568904593639566,"height":12.65625,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":61.39208251090438,"y_image_background":33.68845558166504,"points":[{"x":0,"y":12.098765432098766},{"x":0.7731958762886598,"y":99.50617283950616},{"x":74.22680412371135,"y":100},{"x":75.51546391752578,"y":80.24691358024691},{"x":99.48453608247422,"y":80.49382716049382},{"x":100,"y":0.9876543209876543},{"x":72.68041237113401,"y":0},{"x":72.16494845360825,"y":10.123456790123457}]},{"id":"f3a07bc2-679e-453c-bbb9-4d68dae6096f","title":"Poly","type":"poly","x":69.96098710454395,"y":33.68845558166504,"width":22.41607773851591,"height":17.09375,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":69.96098710454395,"y_image_background":33.68845558166504,"points":[{"x":0.3940886699507389,"y":0.3656307129798903},{"x":0,"y":60.146252285191956},{"x":3.3497536945812803,"y":59.96343692870201},{"x":3.74384236453202,"y":67.27605118829982},{"x":50.24630541871922,"y":67.27605118829982},{"x":50.64039408866995,"y":100},{"x":56.453201970443345,"y":99.6343692870201},{"x":56.65024630541872,"y":85.37477148080438},{"x":59.802955665024626,"y":84.64351005484461},{"x":60.689655172413794,"y":83.54661791590493},{"x":84.43349753694581,"y":83.54661791590493},{"x":84.33497536945814,"y":59.96343692870201},{"x":88.96551724137932,"y":60.3290676416819},{"x":88.76847290640394,"y":33.27239488117002},{"x":97.73399014778326,"y":33.63802559414991},{"x":99.3103448275862,"y":30.895795246800734},{"x":100,"y":27.056672760511884},{"x":98.42364532019704,"y":23.76599634369287},{"x":97.4384236453202,"y":22.6691042047532},{"x":88.96551724137932,"y":22.30347349177331},{"x":88.76847290640394,"y":0}]},{"id":"d364c215-ff0d-4f70-bd03-02dd8ae73c50","title":"Poly","type":"poly","x":79.83289523175243,"y":48.00095558166504,"width":12.522084805653705,"height":14.312499999999993,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":79.83289523175243,"y_image_background":48.00095558166504,"points":[{"x":0,"y":31.877729257641924},{"x":0,"y":100},{"x":80.24691358024691,"y":99.34497816593887},{"x":79.71781305114638,"y":73.58078602620087},{"x":95.06172839506173,"y":73.36244541484717},{"x":99.11816578483244,"y":70.3056768558952},{"x":100,"y":66.8122270742358},{"x":98.4126984126984,"y":62.44541484716157},{"x":94.70899470899471,"y":60.043668122270745},{"x":80.24691358024691,"y":61.135371179039296},{"x":79.71781305114638,"y":28.82096069868996},{"x":72.4867724867725,"y":27.947598253275107},{"x":71.95767195767195,"y":0},{"x":29.98236331569665,"y":0.43668122270742354},{"x":28.92416225749559,"y":1.3100436681222707},{"x":22.57495590828924,"y":1.7467248908296942},{"x":21.516754850088184,"y":19.65065502183406},{"x":12.874779541446207,"y":19.213973799126638},{"x":13.051146384479717,"y":31.877729257641924}]},{"id":"33287708-31af-48b4-b57a-e60d964fa025","title":"Poly","type":"poly","x":63.99808957804218,"y":52.18845558166504,"width":15.878975265017672,"height":10.187500000000007,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":63.99808957804218,"y_image_background":52.18845558166504,"points":[{"x":0,"y":0},{"x":99.44367176634215,"y":0.3067484662576687},{"x":100,"y":99.38650306748467},{"x":0,"y":100}]},{"id":"67acb45a-8bb6-49ab-9c6c-187af773479b","title":"Poly","type":"poly","x":54.61204717521533,"y":45.56345558166504,"width":9.430212014134277,"height":20.3125,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":54.61204717521533,"y_image_background":45.56345558166504,"points":[{"x":60.65573770491803,"y":3.230769230769231},{"x":59.95316159250586,"y":0},{"x":0,"y":1.0769230769230769},{"x":0.234192037470726,"y":82},{"x":76.34660421545667,"y":83.07692307692308},{"x":76.81498829039812,"y":96},{"x":81.49882903981265,"y":99.53846153846155},{"x":85.24590163934425,"y":100},{"x":90.86651053864169,"y":95.84615384615385},{"x":91.33489461358315,"y":82.3076923076923},{"x":100,"y":82.3076923076923},{"x":99.29742388758783,"y":34},{"x":84.07494145199064,"y":34},{"x":83.13817330210773,"y":32.46153846153847},{"x":76.34660421545667,"y":32.46153846153847},{"x":75.64402810304449,"y":27.384615384615387},{"x":54.56674473067916,"y":27.076923076923077},{"x":54.56674473067916,"y":20.46153846153846},{"x":60.187353629976585,"y":19.846153846153847}]},{"id":"80864c1c-09bd-45fd-b0e9-d1479550a2ec","title":"Poly","type":"poly","x":15.417810716393138,"y":45.70169448852539,"width":22.51397740589326,"height":48.83075652887047,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":15.417810716393138,"y_image_background":45.70169448852539,"points":[{"x":0,"y":0.06399655098835894},{"x":0.2942812625537612,"y":54.525061442081814},{"x":49.53734586321611,"y":54.7170510950469},{"x":49.43925210903153,"y":44.98957534481634},{"x":61.01431510281272,"y":45.37355465074649},{"x":60.933853687534025,"y":66.2176193457185},{"x":54.72618921765133,"y":66.336066379522},{"x":54.599240488991974,"y":95.83822776959778},{"x":69.33646180796606,"y":95.76227761587711},{"x":69.78155778814885,"y":100},{"x":99.85944175990893,"y":99.70662643986323},{"x":100,"y":74.72957491780689},{"x":93.57277243441052,"y":74.72279459763118},{"x":93.75459405206315,"y":66.1655214214884},{"x":87.07045073831151,"y":66.04536289774119},{"x":87.40153497846644,"y":61.052709642894435},{"x":87.00915996172809,"y":28.54246174080809},{"x":61.602877627920236,"y":28.47846518981973},{"x":61.50478387373565,"y":41.08578573452644},{"x":49.144970846477776,"y":41.08578573452644},{"x":49.83162712576989,"y":0.12799310197671787},{"x":33.44997017694396,"y":0},{"x":33.54806393112855,"y":1.7279068766856913},{"x":28.643376221899214,"y":1.9198965296507682},{"x":28.15290745097629,"y":0.06399655098835894}]},{"id":"02277662-617d-41a1-abad-d172387992d7","title":"Poly","type":"poly","x":10.700964506439101,"y":13.140985488891602,"width":18.21996466431095,"height":32.59375,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":10.700964506439101,"y_image_background":13.140985488891602,"points":[{"x":66.06060606060606,"y":0},{"x":8.727272727272728,"y":15.340364333652925},{"x":14.666666666666666,"y":28.954937679769895},{"x":1.6969696969696972,"y":32.31064237775647},{"x":0,"y":34.22818791946309},{"x":0.6060606060606061,"y":36.241610738255034},{"x":2.4242424242424243,"y":37.87152444870566},{"x":4.96969696969697,"y":38.25503355704698},{"x":17.333333333333336,"y":34.32406519654842},{"x":38.78787878787879,"y":84.65963566634707},{"x":22.3030303030303,"y":88.97411313518695},{"x":24.96969696969697,"y":94.91850431447747},{"x":25.93939393939394,"y":96.5484180249281},{"x":25.93939393939394,"y":99.80824544582933},{"x":52,"y":100},{"x":51.75757575757576,"y":96.93192713326941},{"x":43.63636363636363,"y":96.74017257909875},{"x":41.6969696969697,"y":91.56279961649089},{"x":51.15151515151515,"y":89.16586768935763},{"x":52.24242424242425,"y":89.93288590604027},{"x":60.60606060606061,"y":87.91946308724832},{"x":60,"y":84.85139022051774},{"x":64.96969696969697,"y":83.02972195589645},{"x":66.42424242424242,"y":85.81016299137104},{"x":100,"y":77.85234899328859}]}]},{"id":"9bacbd67-e914-422a-a9df-dd792e2a09ab","title":"3rd floor","background_type":"image","image_url":"https://i.postimg.cc/Jnkphk7J/Nieuwbouw-03-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"0d112c8c-c537-4f9b-a631-fa7a71d72778","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}},{"id":"ab901fb0-0d64-47c9-b0ec-37d726fc4c1c","title":"kamers 1 ","type":"poly","x":10.670196209695229,"y":13.0699462890625,"width":18.13162544169611,"height":30.6875,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":10.670196209695229,"y_image_background":13.0699462890625,"points":[{"x":8.76979293544458,"y":16.59877800407332},{"x":14.859926918392205,"y":30.65173116089613},{"x":2.192448233861145,"y":34.317718940936864},{"x":0.24360535931790497,"y":36.354378818737274},{"x":0,"y":38.187372708757636},{"x":1.705237515225335,"y":40.224032586558046},{"x":5.115712545676005,"y":40.42769857433808},{"x":17.661388550548114,"y":36.76171079429735},{"x":39.2204628501827,"y":90.52953156822811},{"x":32.64311814859927,"y":91.44602851323829},{"x":36.90621193666261,"y":99.79633401221996},{"x":46.52862362971986,"y":100},{"x":46.52862362971986,"y":97.35234215885947},{"x":60.90133982947626,"y":93.48268839103869},{"x":60.17052375152253,"y":90.12219959266803},{"x":65.6516443361754,"y":88.39103869653768},{"x":67.35688185140073,"y":91.44602851323829},{"x":100,"y":82.28105906313645},{"x":66.86967113276492,"y":0}]},{"id":"6146753e-26bc-4559-a3da-ef5273f6b761","title":"kamers 2","type":"poly","x":15.374259813935511,"y":45.4449462890625,"width":11.064487632508834,"height":26.84375,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"x_image_background":15.374259813935511,"y_image_background":45.4449462890625,"points":[{"x":0.39920159680638717,"y":0.5820721769499418},{"x":0,"y":100},{"x":99.8003992015968,"y":99.53434225844005},{"x":100,"y":0.9313154831199069},{"x":68.06387225548902,"y":0},{"x":67.66467065868264,"y":3.841676367869616},{"x":57.684630738522955,"y":3.841676367869616},{"x":57.28542914171657,"y":0.5820721769499418}]}]},{"id":"0f24d9ab-d895-488c-a0c2-b43ad6cc8520","title":"4th floor","background_type":"image","image_url":"https://i.postimg.cc/PqN6B7BS/Nieuwbouw-04-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"72b69de8-ff56-436b-a0bb-09619555aa01","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}},{"id":"b6478163-cafe-49c1-86d2-8fa072ccb5eb","title":"Kraamzorg","type":"poly","x":10.616303428587228,"y":12.921373070100941,"width":18.28338984445621,"height":31.14406600670157,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"tooltip_content":[{"type":"Heading","text":"Kraamzorg","heading":"h3","other":{"id":"","classes":"","css":""},"style":{"fontFamily":"sans-serif","fontSize":20.8,"lineHeight":"normal","color":"#ffffff","textAlign":"left"},"boxModel":{"width":"auto","height":"auto","margin":{"top":0,"bottom":0,"left":0,"right":0},"padding":{"top":10,"bottom":10,"left":10,"right":10}},"id":"85c3b10c-c69c-4c8d-8e82-017b68b951c8"}],"x_image_background":10.616303428587228,"y_image_background":12.921373070100941,"points":[{"x":8.598726114649681,"y":16.931216931216923},{"x":14.968152866242034,"y":30.952380952380953},{"x":1.9108280254777101,"y":34.39153439153439},{"x":0,"y":37.03703703703704},{"x":0.9554140127388502,"y":39.153439153439166},{"x":3.1847133757961767,"y":40.21164021164022},{"x":17.197452229299362,"y":37.037037037037045},{"x":38.85350318471337,"y":89.41798941798943},{"x":32.80257125466806,"y":90.47619047619048},{"x":35.98725894487486,"y":100},{"x":100,"y":81.48148148148148},{"x":66.2420382165605,"y":0}]},{"id":"8cb88d9c-2908-4d36-9929-b3306dde9dfb","title":"Oncologie","type":"poly","x":15.314996349558124,"y":45.52924776337837,"width":14.24047577670934,"height":26.639344262295076,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"tooltip_content":[{"type":"Heading","text":"Oncologie","heading":"h3","other":{"id":"","classes":"","css":""},"style":{"fontFamily":"sans-serif","fontSize":20.8,"lineHeight":"normal","color":"#ffffff","textAlign":"left"},"boxModel":{"width":"auto","height":"auto","margin":{"top":0,"bottom":0,"left":0,"right":0},"padding":{"top":10,"bottom":10,"left":10,"right":10}},"id":"64b7f385-a51e-463c-9df4-6cfd5f368919"}],"x_image_background":15.314996349558124,"y_image_background":45.52924776337837,"points":[{"x":0.3389830508474576,"y":0.5128205128205128},{"x":0,"y":100},{"x":78.30508474576271,"y":100},{"x":78.30508474576271,"y":82.3076923076923},{"x":96.61016949152543,"y":82.05128205128204},{"x":99.32203389830508,"y":79.48717948717949},{"x":100,"y":76.92307692307693},{"x":95.59322033898306,"y":75.38461538461539},{"x":77.62711864406779,"y":74.87179487179488},{"x":77.62711864406779,"y":0}]}]},{"id":"8d9e9f65-bd45-4397-a55c-52a0f7a5f8a8","title":"5th floor","background_type":"image","image_url":"https://i.postimg.cc/7PSB80Wr/Nieuwbouw-05-1.jpg","width":1132,"height":800,"use_image_size":true,"children":[{"id":"3cbf0a60-7cb6-4311-9d06-61de49be7b96","title":"Spot","x":5.123230245789743,"y":11.967330932617188,"default_style":{"icon_size":52,"icon_svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 512\"><!--! Font Awesome Free 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc. --><path d=\"M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z\"/></svg>","icon_fill":"#0062ff"},"mouseover_style":{"icon_fill":"#4ddbff"},"actions":{"click":"change-artboard","artboard":"default-id"}},{"id":"23c31e62-b154-4f0a-9653-6da031a79bbb","title":"kamers 1","type":"poly","x":10.626394588618734,"y":12.98843193054199,"width":18.264134275618375,"height":31.375,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"actions":{"script":"console.log('this is rooms 1')"},"x_image_background":10.626394588618734,"y_image_background":12.98843193054199,"points":[{"x":9.4316807738815,"y":16.235059760956176},{"x":15.840386940749699,"y":30.1792828685259},{"x":1.9347037484885126,"y":34.36254980079681},{"x":0,"y":36.852589641434264},{"x":0.6045949214026602,"y":38.745019920318725},{"x":4.353083434099154,"y":40.1394422310757},{"x":17.17049576783555,"y":35.95617529880478},{"x":38.57315598548972,"y":88.54581673306772},{"x":33.252720677146314,"y":90.0398406374502},{"x":35.18742442563482,"y":94.42231075697211},{"x":38.21039903264813,"y":97.70916334661355},{"x":43.772672309552604,"y":96.01593625498009},{"x":45.58645707376058,"y":99.9003984063745},{"x":59.6130592503023,"y":100},{"x":60.45949214026602,"y":88.94422310756973},{"x":65.2962515114873,"y":87.74900398406375},{"x":67.59371221281741,"y":89.34262948207171},{"x":66.98911729141476,"y":98.20717131474103},{"x":86.57799274486095,"y":98.70517928286853},{"x":86.21523579201936,"y":84.26294820717132},{"x":100,"y":80.47808764940238},{"x":66.50544135429263,"y":0}]},{"id":"fca476ca-b860-46d5-9166-cc3da040f304","title":"kamers 2","type":"poly","x":15.330458192859018,"y":43.050933837890625,"width":11.130742049469964,"height":29.0625,"default_style":{"background_color":"#ffffff","background_opacity":0.036315522869333206},"mouseover_style":{"background_color":"#ff8800","background_opacity":0.5421521087557842,"stroke_color":"#c75757","stroke_width":4},"actions":{"script":"afdeling = 'Chirurgie'"},"x_image_background":15.330458192859018,"y_image_background":43.050933837890625,"points":[{"x":28.57142857142857,"y":0},{"x":16.666666666666664,"y":3.763440860215054},{"x":15.873015873015872,"y":9.032258064516128},{"x":0.5952380952380952,"y":8.817204301075268},{"x":0,"y":100},{"x":100,"y":100},{"x":99.8015873015873,"y":8.60215053763441},{"x":67.85714285714286,"y":9.247311827956988},{"x":68.25396825396825,"y":11.720430107526882},{"x":58.53174603174603,"y":11.720430107526882},{"x":58.53174603174603,"y":8.9247311827957},{"x":42.857142857142854,"y":8.38709677419355},{"x":41.86507936507937,"y":4.623655913978494},{"x":32.142857142857146,"y":4.623655913978494}]}]}],"version":"6.0.30"})
    addClickFunctions()
  } else {
    console.error('Image Map Pro script not loaded.')
  }
}

function addClickFunctions() {
  if (window.ImageMapPro) {
    window.ImageMapPro.subscribe((action) => {
      if (action.type === 'artboardChange' && action.payload.artboard === 'default-id') {
        console.log('succes')
        afdeling.value = 'Overzicht'
      }
    })

    window.ImageMapPro.subscribe((action) => {
      if (action.type === 'objectClick' && action.payload.object === 'Kraamzorg') {
        afdeling.value = 'Verloskunde'
      }
    })
  }
}

onMounted(() => {
  // Check if Image Map Pro is available
  if (window.ImageMapPro) {
    initializeImageMapPro() // Initialize directly if script is already loaded
  } else {
    // If the script isn't loaded yet, listen for the `window.onload` event
    window.onload = initializeImageMapPro
  }
})

const options = [
  'Overzicht',
  'Spoedeisende Hulp',
  'Chirurgie',
  'Geriatrie',
  'Kardiochirurgie',
  'Verloskunde',
  'Oncologie',
  'Pediatrie',
  'Psychiatrie',
]
const afdeling = defineModel('afdeling')
provide('afdeling', afdeling)
onMounted(() => {
  // Set the first default value from the list
  afdeling.value = options[0]
  selectedButtoneStore.currentDepartment = 'Overzicht'
})
const sortChoice = ref(null)
// a save location for the previous sorting choice to permit sorting in reverse

function filterAllInfusions(afdeling) {
  selectedButtoneStore.currentDepartment = afdeling
  currentInfusions = AllInfusions.filter((infusion) => infusion.department === afdeling)
}
function returnToAllInfusions() {
  selectedButtoneStore.currentDepartment = 'Overzicht'
  currentInfusions = AllInfusions
}
watch(selectedButtoneStore.currentDepartment, (newAfdeling) => {
  if (newAfdeling === 'Overzicht') {
    returnToAllInfusions()
    return
  }
  filterAllInfusions(newAfdeling)
})

watch(afdeling, (newAfdeling) => {
  if (newAfdeling === 'Overzicht') {
    returnToAllInfusions()
    return
  }
  filterAllInfusions(newAfdeling)
})

function FilterNonRun() {
  currentInfusions = currentInfusions.filter(
    (infusion) => infusion.timeRemaining === 'Infusion not running',
  )
}

function FilterBelow10() {
  currentInfusions = currentInfusions.filter(
    (infusion) => infusion.totalMl / infusion.remainingMl > 10,
  )
}

function FilterLessThenHour() {
  currentInfusions = currentInfusions.filter((infusion) => {
    if (!(infusion.timeRemaining === 'Infusion not running')) {
      var splitstring = infusion.timeRemaining.split(':')
      if (splitstring[0] === '0') {
        return infusion
      }
    }
  })
}

function excecuteFilters() {
  toggleStateMultiple.value.forEach(filterIt)
}
function filterIt(value) {
  switch (true) {
    case value === 'nonRun':
      FilterNonRun()
      return
    case value === 'below10':
      FilterBelow10()
      return
    case value === '1hour':
      FilterLessThenHour()
      return
    case value === 'reset':
      returnToAllInfusions()
      sortInfusions(sortChoice.value)
  }
}

function calculatePercentage(infusion) {
  return parseFloat(((infusion.remainingMl / infusion.totalMl) * 100).toFixed(1))
}

function timeToSeconds(time) {
  // Ensure the time has a valid format like HH:SS
  const [hours, seconds] = time.split(':').map(Number)

  // Calculate the total time in minutes (convert to seconds if needed)
  return hours * 60 + seconds // Convert to total minutes (HH treated as minutes)
}

function sortInfusions(newSortChoice) {
  switch (true) {
    case newSortChoice === 'remainingMl':
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = calculatePercentage(currentInfusions[j])
          const value2 = calculatePercentage(currentInfusions[j + 1])
          if (value1 > value2) {
            const temp = currentInfusions[j]
            currentInfusions[j] = currentInfusions[j + 1]
            currentInfusions[j + 1] = temp
          }
        }
      }
      if (toggleState.value === true) {
        reverse()
      }
      return
    case newSortChoice === 'time':
      currentInfusions.sort((a, b) => {
        // If 'Infusion not running', treat it as the largest possible time value
        const timeA = a.timeRemaining === 'Infusion not running' ? '9999:59' : a.timeRemaining
        const timeB = b.timeRemaining === 'Infusion not running' ? '9999:59' : b.timeRemaining

        // Normalize the time (pad single-digit hours) before calculating the seconds
        const normalizedTimeA = timeA.length < 5 ? `0${timeA}` : timeA
        const normalizedTimeB = timeB.length < 5 ? `0${timeB}` : timeB

        // Compare by total seconds (timeToSeconds) but treat 'Infusion not running' as the last
        return timeToSeconds(normalizedTimeA) - timeToSeconds(normalizedTimeB)
      })
      if (toggleState.value === true) {
        reverse()
      }
      return
    case newSortChoice === 'ward': {
      currentInfusions = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.ward > curr.ward)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      if (toggleState.value === true) {
        reverse()
      }
      return
    }
    case newSortChoice === 'bed': {
      currentInfusions = currentInfusions.reduce((acc, curr) => {
        let ind = acc.findIndex((item) => item.bed > curr.bed)
        if (ind === -1) ind = acc.length
        acc.splice(ind, 0, curr)
        currentInfusions = acc
        return acc
      }, [])
      if (toggleState.value === true) {
        reverse()
      }
      return
    }
    case newSortChoice === 'drug':
      for (let i = 0; i < currentInfusions.length; i++) {
        for (let j = 0; j < currentInfusions.length - 1 - i; j++) {
          const value1 = Object.values(currentInfusions[j])[3]
          const value2 = Object.values(currentInfusions[j + 1])[3]
          if (value1 > value2) {
            const temp = currentInfusions[j]
            currentInfusions[j] = currentInfusions[j + 1]
            currentInfusions[j + 1] = temp
          }
        }
      }
      if (toggleState.value === true) {
        reverse()
      }
      return
  }
}

watch(sortChoice, (newSortChoice) => {
  sortInfusions(newSortChoice)
})

const toggleStateMultiple = ref(['reset'])
const toggleState = ref(false)

watch(toggleState, () => {
  reverse()
})

watch(toggleStateMultiple, (newToggleStateMultiple) => {
  excecuteFilters(newToggleStateMultiple)
})

function reverse() {
  currentInfusions = currentInfusions.reverse()
}
const toggleGroupItemClasses =
  'hover:bg-gray-100  data-[state=on]:bg-blue-500 data-[state=on]:text-white  flex h-[35px] xl:w-[20vw] md:w-[35vw] w-[30vw] items-center justify-center bg-white text-base leading-4 first:rounded-l last:rounded-r focus:z-10 focus:shadow-[0_0_0_2px] focus:shadow-black focus:outline-none dark:bg-gray-300  dark:border-gray-600 dark:hover:bg-gray-400 dark:data-[state=on]:bg-gray-400 '
</script>

<template>
  <body class="bg-white dark:bg-black">
    <header class="md:flex h-[8vh] bg-blue-500 p-6 md:overflow-hidden">
      <img
        src="./assets/LumiadLogo.svg"
        alt="logo"
        class="md:mr-[30vw] md:h-[2vw] md:visible invisible"
      />
      <img
        src="./assets/dashboardnaam.svg"
        alt="logo"
        class="relative md:mr-[24vw] mr-[4vw] md:visible invisible h-[3vw]"
      />
      <select
        v-model="afdeling"
        class="md:flex md:static absolute top-3 left-18 w-[70vw] md:w-full bg-gray-50 border border-gray-300 hover:bg-gray-100 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-300 dark:border-gray-600 dark:hover:bg-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
      >
        <option
          v-for="(option, index) in options"
          :value="option"
          :key="index"
          v-bind:selected="index === 0"
        >
          {{ option }}
        </option>
      </select>
    </header>
    <section class="xl:flex 4xl:h-[78.9vh] xl:h-[75vh] overflow-hidden dark:bg-black">
      <div
        class="xl:m-3 xl:h-[77vh] h-[0vh] xl:w-[70vw] relative md:rounded-[1vw] bg-gray-200 dark:bg-gray-500 p-2 xl:visible invisible"
      >
        <div
          class="4xl:w-[40.5vw] xl:w-[54vw] outline-8 rounded-xl outline-gray-500 relative 4xl:left-1/5 4xl:top-2 xl:left-36 xl:top-4"
        >
          <div id="image-map-pro"></div>
        </div>
      </div>
      <div
        class="xl:w-[30vw] 4xl:h-[77vh] xl:h-[75vh] m-3 flex-initial bg-gray-200 dark:bg-gray-500 md:rounded-[1vw] rounded-[3vw] p-2 overflow-x-hidden"
      >
        <div>
          <ToggleGroupRoot v-model="toggleStateMultiple" type="multiple" class="flex">
            <ToggleGroupItem value="nonRun" :class="toggleGroupItemClasses">
              Non-running
            </ToggleGroupItem>
            <ToggleGroupItem value="below10" :class="toggleGroupItemClasses">
              below 10%
            </ToggleGroupItem>
            <ToggleGroupItem value="1hour" :class="toggleGroupItemClasses">
              Less then 1 hour
            </ToggleGroupItem>
          </ToggleGroupRoot>
        </div>
        <div class="grid grid-cols-8">
          <select
            v-model="sortChoice"
            class="w-[78vw] col-span-7 xl:w-full bg-gray-50 border border-gray-300 hover:bg-gray-100 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-300 dark:border-gray-600 dark:hover:bg-gray-400 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
          >
            <option selected disabled>Sort by</option>
            <option value="remainingMl">remaining %IV</option>
            <option value="time">Remaining time</option>
            <option value="ward">Ward</option>
            <option value="bed">bed</option>
            <option value="drug">Drug</option>
          </select>
          <Toggle
            v-model:pressed="toggleState"
            aria-label="Toggle italic"
            class="hover:bg-gray-100 text-black data-[state=on]:bg-blue-500 data-[state=on]:text-white flex items-center justify-center rounded bg-gray-50 border border-gray-300"
          >
            <Icon icon="radix-icons:caret-sort" class="color-black" />
          </Toggle>
        </div>

        <div
          class="4xl:m-3 md:m-1 m-2 4xl:h-[68vh] xl:h-[60vh] md:h-[60.2vh] h-[51.3vh] xl:w-[28vw] overflow-auto"
        >
          <div v-for="infusion in currentInfusions" :key="infusion.id + Math.random()">
            <InfusionButtons
              :department="infusion.department"
              :ward="infusion.ward"
              :bed="infusion.bed"
              :drug="infusion.drug"
              :status="infusion.status"
              :totalMl="infusion.totalMl"
              :remainingMl="infusion.remainingMl"
              :mlPerHour="infusion.mlPerHour"
              :time-running="infusion.timeRunning"
              :timeRemaining="infusion.timeRemaining"
              :id="infusion.id"
            />
          </div>
        </div>
      </div>
    </section>
    <section class="xl:flex overflow-hidden dark:bg-black">
      <div
        class="xl:m-3 4xl:h-[11.25vh] xl:static xl:h-[14.5vh] 4XL:w-[100vw] xl:w-[100vw] flex-initial md:rounded-[1vw] rounded-[3vw] bg-gray-200 dark:bg-gray-500"
      >
        <div
          id="infuusDetails"
          class="4XL:w-[98vw] xl:static xl:w-[96vw] flex-initial overflow-hidden rounded-[2vw] p-5 font-[Open_Sans] text-2xl text-ellipsis [&::-webkit-scrollbar]:[width:10px] [&::-webkit-scrollbar]:rounded-full [&::-webkit-scrollbar-thumb]:bg-gray-400"
        >
          <RouterView />
        </div>
      </div>
    </section>
  </body>
</template>

<style scoped></style>
