<template>
  <div class="container">
    <div class="row">
      <br><br>
      <h1>Счета</h1>
      <div class="col-sm-10">
        <hr><br><br>
        <table class="table table-hover" id="PaymentAccounts">
          <thead>
            <tr>
              <th scope="col">Номер счёта</th>
              <th scope="col">Сумма</th>
              <th scope="col">Статус</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(pay_account, index) in payment_accounts" :key="index">
              <td>{{ pay_account.account_number }}: {{ pay_account.service_name }}
                <br>
                {{ pay_account.adress }}
                <br>
                <span class="text-muted" >{{ pay_account.date }}</span>
                </td>
              <td>{{ pay_account.amount }}</td>
              <td v-if="(pay_account.status === true)">Оплачен
                <br>
                <button class="btn btn-secondary" type="submit" @click="sendMail">Выслать детализацию счета на почту</button>
              </td>
              <td v-else>Не оплачен</td>
            </tr>
          </tbody>
        </table>
        <b-pagination
          v-model="page"
          :total-rows="count"
          :per-page="pageSize"
          aria-controls="PaymentAccounts"
          @change="handlePageChange"
          @click="getPaymentAccounts"
      ></b-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PaymentAccounts',
  data() {
    return {
      payment_accounts: [],
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
    getPaymentAccounts() {
      const params = this.getRequestParams(
        this.page,
        this.pageSize
      );
      const path = 'http://127.0.0.1:5000/api/payment_accounts/';
      axios.get(path, { params: params })
        .then((res) => {
          this.payment_accounts = res.data.results;
          this.count = res.data.totalElements;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    sendMail() {
      const path = 'http://127.0.0.1:5000/api/send_detail_for_current_account/'
       axios.get(path)
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
    this.getPaymentAccounts();
  }
};
</script>