<template lang="html">
  <section class="dashboard">
    <div class="row">
      <div class="col-xl-3 col-sm-6 grid-margin stretch-card">
        <div class="card card-statistics">
          <div class="card-body">
            <div class="d-flex justify-content-between flex-wrap">
              <div>
                <i class="mdi mdi-receipt text-warning icon-lg"></i>
              </div>
              <div>
                <p class="card-text text-right">Today Orders</p>
                <div class="fluid-container">
                  <h3 class="card-title font-weight-bold text-right mb-0">55</h3>
                </div>
              </div>
            </div>
            <p class="text-muted mt-3">
              <i class="mdi mdi-bookmark-outline mr-1" aria-hidden="true"></i> Product-wise sales
            </p>
          </div>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 grid-margin stretch-card">
        <div class="card card-statistics">
          <div class="card-body">
            <div class="d-flex justify-content-between flex-wrap">
              <div>
                <i class="mdi mdi-cube text-danger icon-lg"></i>
              </div>
              <div>
                <p class="card-text text-right">Total Revenue</p>
                <div class="fluid-container">
                  <h3 class="card-title font-weight-bold text-right mb-0">5,065,650 VND</h3>
                </div>
              </div>
            </div>
            <p class="text-muted mt-3">
              <i class="mdi mdi-alert-octagon mr-1" aria-hidden="true"></i> 65% lower growth
            </p>
          </div>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 grid-margin stretch-card">
        <div class="card card-statistics">
          <div class="card-body">
            <div class="d-flex justify-content-between flex-wrap">
              <div>
                <i class="mdi mdi-poll-box text-teal icon-lg"></i>
              </div>
              <div>
                <p class="card-text text-right">Total Expenses</p>
                <div class="fluid-container">
                  <h3 class="card-title font-weight-bold text-right mb-0">2,030,650 VND</h3>
                </div>
              </div>
            </div>
            <p class="text-muted mt-3">
              <i class="mdi mdi-calendar mr-1" aria-hidden="true"></i> Weekly Sales
            </p>
          </div>
        </div>
      </div>
      <div class="col-xl-3 col-sm-6 grid-margin stretch-card">
        <div class="card card-statistics">
          <div class="card-body">
            <div class="d-flex justify-content-between flex-wrap">
              <div>
                <i class="mdi mdi-account-location text-info icon-lg"></i>
              </div>
              <div>
                <p class="card-text text-right">Employees</p>
                <div class="fluid-container">
                  <h3 class="card-title font-weight-bold text-right mb-0">1</h3>
                </div>
              </div>
            </div>
            <p class="text-muted mt-3">
              <i class="mdi mdi-reload mr-1" aria-hidden="true"></i> Product-wise sales
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 grid-margin">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4">Orders</h5>
            <div class="table-responsive">
              <table class="table center-aligned-table">
                <thead>
                  <tr>
                    <th class="border-bottom-0">Order No</th>
                    <th class="border-bottom-0">Product Name</th>
                    <th class="border-bottom-0">Purchased On</th>
                    <th class="border-bottom-0">Shipping Status</th>
                    <th class="border-bottom-0">Payment Method</th>
                    <th class="border-bottom-0">Payment Status</th>
                    <th class="border-bottom-0"></th>
                    <th class="border-bottom-0"></th>
                    <th class="border-bottom-0"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>034</td>
                    <td>Black Coffee</td>
                    <td>12 Jun 2020</td>
                    <td>Dispatched</td>
                    <td>Credit card</td>
                    <td><label class="badge badge-teal">Approved</label></td>
                    <td><a href="#" class="btn btn-outline-success btn-sm">View Order</a></td>
                    <td><a href="#" class="btn btn-outline-danger btn-sm">Cancel</a></td>
                  </tr>
                  <tr>
                    <td>035</td>
                    <td>Espresso</td>
                    <td>15 Jun 2020</td>
                    <td>Dispatched</td>
                    <td>Internet banking</td>
                    <td><label class="badge badge-warning">Pending</label></td>
                    <td><a href="#" class="btn btn-outline-success btn-sm">View Order</a></td>
                    <td><a href="#" class="btn btn-outline-danger btn-sm">Cancel</a></td>
                  </tr>
                  <tr>
                    <td>036</td>
                    <td>Flat White</td>
                    <td>17 Jun 2020</td>
                    <td>Dispatched</td>
                    <td>Credit card</td>
                    <td><label class="badge badge-teal">Approved</label></td>
                    <td><a href="#" class="btn btn-outline-success btn-sm">View Order</a></td>
                    <td><a href="#" class="btn btn-outline-danger btn-sm">Cancel</a></td>
                  </tr>
                  <tr>
                    <td>037</td>
                    <td>Cappuccino</td>
                    <td>17 Jun 2020</td>
                    <td>Dispatched</td>
                    <td>Cash on delivery</td>
                    <td><label class="badge badge-danger">Rejected</label></td>
                    <td><a href="#" class="btn btn-outline-success btn-sm">View Order</a></td>
                    <td><a href="#" class="btn btn-outline-danger btn-sm">Cancel</a></td>
                  </tr>
                  <tr>
                    <td>038</td>
                    <td>Macchiato Coffee</td>
                    <td>19 Jun 2020</td>
                    <td>Dispatched</td>
                    <td>Debit card</td>
                    <td><label class="badge badge-teal">Approved</label></td>
                    <td><a href="#" class="btn btn-outline-success btn-sm">View Order</a></td>
                    <td><a href="#" class="btn btn-outline-danger btn-sm">Cancel</a></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="js">
export default {
  name: 'dashboard'
}
</script>

<style scoped lang="scss">
</style>
