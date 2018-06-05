package id.web.singgi.tugas10

class ArrayModel{

    var rowId:Int = 0
    var lokasi: String = ""
    var long: String = ""
    var lat: String = ""

    constructor(rowId: Int, lokasi: String, long: String, lat: String) {
        this.rowId = rowId
        this.lokasi = lokasi
        this.long = long
        this.lat = lat
    }

    constructor(lokasi: String,long: String,lat: String) {
        this.lokasi = lokasi
        this.long = long
        this.lat = lat
    }
}