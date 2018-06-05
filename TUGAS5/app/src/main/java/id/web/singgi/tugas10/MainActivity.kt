package id.web.singgi.tugas10

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*
import kotlin.collections.ArrayList

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //inisialisasi tanggal
        val c:Calendar = Calendar.getInstance()
        val year:Int = c.get(Calendar.YEAR)
        val month:Int = c.get(Calendar.MONTH)
        val day:Int = c.get(Calendar.DAY_OF_MONTH)

        //menampilkan tanggal
        TANGGAL.text = "$day/$month/$year"

        fun readData(): MutableList<ArrayModel> {
            val list = ArrayList<ArrayModel>()
            val teks: String = Lokasi.text.toString()
            list.add(ArrayModel(rowId = 1, lokasi = "ITATS", long = "-7.289241", lat = "112.778776" ))
            list.add(ArrayModel(rowId = 2, lokasi = "Narotama", long = "-7.288075", lat = "112.776449" ))
            for (n: ArrayModel in list) {
                if (teks == n.lokasi) {
                    LONG.setText(n.long)
                    LAT.setText(n.lat)
                    Toast.makeText(this,"Data ditemukan",Toast.LENGTH_SHORT).show
                }
            }
            return list
        }

        //memanggil fungsi arraylist
        tampil.setOnClickListener{readData()}

        //fungsi tombol clearall
        fun clearData() {
            Lokasi.setText("")
            LONG.setText("")
            LAT.setText("")
        }

        //memanggil fungsi clear all
        clearall.setOnClickListener{clearData()}

        //memindah activity_main ke map ITATS
        itats.setOnClickListener {
            val maintomap = Intent(this, MapsActivity::class.java )
        }

        //memindah activity_main ke map NAROTAMA
        unnar.setOnClickListener {
            val maintomap = Intent(this, MapsActivity::class.java )
        }
    }
}
