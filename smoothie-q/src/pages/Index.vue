<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <div class="q-gutter-y-md" style="max-width: 700px">
        <q-card>
          <q-tabs
            v-model="tab"
            dense
            class="text-grey"
            active-color="primary"
            indicator-color="primary"
            align="justify"
            narrow-indicator
          >
            <q-tab name="all" label="All"></q-tab>
            <q-tab name="only" label="Only"></q-tab>
            <q-tab name="random" label="Random"></q-tab>
          </q-tabs>

          <q-separator></q-separator>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="all">
              <div class="text-h6">All</div>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
            </q-tab-panel>

            <q-tab-panel name="only">
              <div class="text-h6">Only</div>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
            </q-tab-panel>

            <q-tab-panel name="random">
              <div class="text-h6">Random</div>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
            </q-tab-panel>
          </q-tab-panels>
        </q-card>
        <q-card class="q-pa-md">
          <q-infinite-scroll @load="onLoad" :offset="250">
            <div v-for="(item, index) in items" :key="index" class="caption">
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
                repellendus sit voluptate voluptas eveniet porro. Rerum
                blanditiis perferendis totam, ea at omnis vel numquam
                exercitationem aut, natus minima, porro labore.
              </p>
            </div>
            <template v-slot:loading>
              <div class="row justify-center q-my-md">
                <q-spinner-dots color="primary" size="40px"></q-spinner-dots>
              </div>
            </template>
          </q-infinite-scroll>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",
  data() {
    return {
      tab: "all",
      items: [{}, {}, {}, {}, {}, {}, {}],
    };
  },
  methods: {
    onLoad(index, done) {
      setTimeout(() => {
        if (this.items) {
          this.items.push({}, {}, {}, {}, {}, {}, {});
          done();
        }
      }, 2000);
    },
  },
};
</script>
