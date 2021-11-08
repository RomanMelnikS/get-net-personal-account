<template>
  <div class="container">
    <div class="row">
      <br><br>
      <h1>Линии</h1>
      <div class="col-sm-10">
        <hr><br><br>
        <table class="table table-hover" id="lines">
          <thead>
            <tr>
              <th scope="col">Тип линии</th>
              <th scope="col">CLI</th>
              <th scope="col">Город</th>
              <th scope="col">Тариф</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(line, index) in lines" :key="index">
              <td>{{ line.type_of_line }}</td>
              <td>{{ line.cli }}</td>
              <td>{{ line.city }}</td>
              <td>{{ line.tariff }}</td>
            </tr>
          </tbody>
        </table>
        <b-pagination
          v-model="page"
          :total-rows="count"
          :per-page="pageSize"
          aria-controls="Lines"
          @change="handlePageChange"
          @click="getLines"
        ></b-pagination>
      </div>
    </div>
</div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'Lines',
  data() {
    return {
      lines: [],
      page: 1,
      count: 0,
      pageSize: 5,
    };
  },
  methods: {
    getRequestParams( page, pageSize ) {
      let params = {};

      if (page) {
        params["page"] = page;
      }

      if (pageSize) {
        params["size"] = pageSize;
      }

      return params;
    },
    getLines() {
      const params = this.getRequestParams(
        this.page,
        this.pageSize
      );
      const path = 'http://127.0.0.1:5000/api/lines/';
      axios.get(path, { params: params })
        .then((res) => {
          this.lines = res.data.results;
          this.count = res.data.totalElements;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handlePageChange(value) {
      this.page = value;
      this.getLines();
    }
  },
  created() {
    this.getLines();
  }
};
</script>
