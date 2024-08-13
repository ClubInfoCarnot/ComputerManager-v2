<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/computers.css">
    <title>Ordinateurs</title>
</head>
<body>

    <section class="research">
        <h2 class="research-h2">Recherche</h2>
        <div class="research-div">
            <input type="text" name="research" id="research" class=research-input>
            <a href="#" action="">Rechercher</a>
        </div>
    </section>

    <section class="result">
        <table class="computer-result-table">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">N° de série</th>
                <th scope="col">Marque</th>
                <th scope="col">Modèle</th>
                <th scope="col">Adresse MAC</th>
                <th scope="col">Arrivée</th>
                <th scope="col">Départ</th>
                <th scope="col">Destinataire</th>
                <th scope="col">Status</th>
            </tr>
            <tr>
                <th scope=\"row\">".$computer->id."</th>
                <td>".$computer->serialNumber."</td>
                <td>".$computer->brand."</td>
                <td>".$computer->model."</td>
                <td>".$computer->macAddress."</td>
                <td>".$computer->entryDate."</td>
                <td>".$computer->exitDate."</td>
                <td>".$computer->recipient->name."</td>
                <td class=\"status\">".$state."</td>
            </tr>;
        </table>
    </section>
    
</body>
</html>