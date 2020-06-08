
<template>
    <section class="staffs">
        <div class = "card">
          <div class = "card-body">
            <b-col lg="12" md="12" class="my-1">
              <b-form-group
                label="Search"
                label-cols-sm="3"
                label-align-sm="right"
                label-size="sm"
                label-for="filterInput"
                class="mb-0"
              >
                <div class="row">
                  <div class="col-sm-4">
                    <b-input-group size="md">
                      <b-form-input
                      v-model="filter"
                      type="search"
                      id="filterInput"
                      placeholder="Type to Search"
                      ></b-form-input>
                    </b-input-group>
                  </div>
                  <div class="col-sm-4"></div>
                  <div class="col-sm-4">
                    <b-input-group size="md">
                      <b-button variant="primary" style="margin-left:30px">New Staff</b-button>
                      <b-button variant="success" style="margin-left:30px">Export</b-button>
                    </b-input-group>
                  </div>
                </div>
              </b-form-group>
            </b-col>
          </div>
        </div>
        <div class = "card">
          <div class = "card-body">
            <b-table
            :items="items"
            :fields="fields"
            :sort-by.sync="sortBy"
            :sort-desc.sync="sortDesc"
            :filter="filter"
            :currentPage="currentPage"
            :per-page="perPage"
            @filtered="onFiltered"
            responsive="sm"
            bordered
            >
              <template #Image="{item}">
                  <img
                    height="65"
                    v-bind:src="item.Image"
                    onclick="window.open(this.src)"
                    style="cursor: pointer;"
                  />
              </template>
              <template style="width:20px" #Edit>
                  <b-button variant="outline-primary" class=" btn-inverse-primary">Edit</b-button>
              </template>
              <template #Delete>
                  <b-button  variant="outline-danger" class=" btn-inverse-danger">Delete</b-button>
              </template>
            </b-table>
            <b-row>
              <b-col class="col-md-4 col-sm-6 grid-margin stretch-card" style="padding-top: 15px;">
                <b-form-group
                  label="Item per page"
                  label-cols-sm="6"
                  label-cols-md="4"
                  label-cols-lg="3"
                  label-align-sm="right"
                  label-size="sm"
                  label-for="perPageSelect"
                  class="mb-0"
                >
                  <b-form-select
                    v-model="perPage"
                    id="perPageSelect"
                    :options="pageOptions"
                  ></b-form-select>
                </b-form-group>
              </b-col>
              <b-col>
                <div class="col-md-4 col-sm-6 grid-margin stretch-card">
                  <div class="card">
                    <div class="card-body">
                      <b-pagination align="right" :total-rows="totalRows" v-model="currentPage" :per-page="perPage">
                      </b-pagination>
                    </div>
                  </div>
                </div>
              </b-col>
            </b-row>
          </div>
        </div>
    </section>
</template>

<script lang="js">
import { getAPI } from "../../../api/axios-base.js";
import { mapState } from "vuex";
import swal from "sweetalert2";
let config = {
  headers: {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*',
  }
}
const genders = [
  { value: "Female", label: "Female" },
  { value: "Male", label: "Male" }
];
var items = [];
export default {
  name: 'staffs',
  data () {
    return {
      sortBy: 'age',
      sortDesc: false,
      fields: [
        { key: 'StaffId', label: 'Staff ID', sortable: true },
        { key: 'FullName', label: 'Name', sortable: true },
        { key: 'DateOfBirth', label: 'Date of Birth', sortable: false },
        { key: 'Gender', label: 'Gender', sortable: false },
        { key: 'Phone', label: 'Phone Number', sortable: false },
        { key: 'Image', label: 'Profile Image', sortable: false },
        { key: 'PositionName', label: 'Position', sortable: false },
        { key: 'Edit', label: 'Edit', sortable: false, tdClass: 'table-button' },
        { key: 'Delete', label: 'Delete', sortable: false, tdClass: 'table-button' }
      ],
      items: items.map(item => {
        return { ...item };
      }),
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 50],
      filter: null,
      filterOn: []
    }
  },
  mounted(){
    this.totalRows = this.items.length
    console.log(this.totalRows)
  },
  methods: {
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length
      this.currentPage = 1
    },
    getStaff() {
      getAPI
        .get("/staff", config)
        .then(response => {
          this.items = response.data;
          console.log("Data loading success");
          console.log(this.items);
        })
        .catch(err => {
          console.log(err);
          swal.fire({
            toast: true,
            position: "top-end",
            icon: "error",
            title: "Error",
            text: "Network error",
            showConfirmButton: false,
            timer: 3000
          });
        });
    }
  },
  created() {
    this.getStaff();
  },
}
</script>
