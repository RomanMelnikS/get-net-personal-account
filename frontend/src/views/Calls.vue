<template>
  <div class="container">
    <div class="row">
      <br><br>
      <h1>Звонки</h1>
      <div class="col-sm-10">
        <hr><br><br>
        <table class="table table-hover" id="Calls">
          <thead>
            <tr>
              <th scope="col">Направление</th>
              <th scope="col">Дата</th>
              <th scope="col">Продолжительность</th>
              <th scope="col">Стоимость</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(call, index) in calls" :key="index">
              <td>{{ call.direction }}</td>
              <td>{{ call.date }}</td>
              <td>{{ call.duration }} мин.</td>
              <td>{{ call.cost }} руб./мин.</td>
            </tr>
          </tbody>
        </table>
        <b-pagination
          v-model="page"
          :total-rows="count"
          :per-page="pageSize"
          aria-controls="Calls"
          @change="handlePageChange"
          @click="getCalls"
        ></b-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Calls',
  data() {
    return {
      calls: [],
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
    getCalls() {
      const params = this.getRequestParams(
        this.page,
        this.pageSize
      );
      const path = 'http://127.0.0.1:5000/api/calls/';
      axios.get(path, { params: params })
        .then((res) => {
          this.calls = res.data.results;
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
    this.getCalls();
  }
};
</script>