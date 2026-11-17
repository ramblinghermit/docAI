<template>
  <div id="univer-container" style="width: 100vw; height: 100vh;"></div>
</template>

<script setup>
import { onMounted } from 'vue'
import {
  Univer,
  LocaleType,
  ICommandService,
} from '@univerjs/core'
import { defaultTheme } from '@univerjs/design'
import { UniverRenderEnginePlugin } from '@univerjs/engine-render'
import { UniverFormulaEnginePlugin } from '@univerjs/engine-formula'
import { UniverEditorPlugin } from '@univerjs/editor'
import { UniverUIPlugin } from '@univerjs/ui'
import { UniverSheetsPlugin } from '@univerjs/sheets'
import { UniverSheetsUIPlugin } from '@univerjs/sheets-ui'
import { UniverSheetsFormulaPlugin } from '@univerjs/sheets-formula'
import { UniverFindReplacePlugin } from '@univerjs/find-replace'

onMounted(() => {
  const univer = new Univer({
    theme: defaultTheme,
    locale: LocaleType.EN_US,
  })

  // 🔹 Register plugins in correct dependency order
  univer.registerPlugin(UniverRenderEnginePlugin)
  univer.registerPlugin(UniverFormulaEnginePlugin)
  univer.registerPlugin(UniverEditorPlugin)
  univer.registerPlugin(UniverUIPlugin)
  univer.registerPlugin(UniverSheetsPlugin)
  univer.registerPlugin(UniverSheetsUIPlugin)
  univer.registerPlugin(UniverSheetsFormulaPlugin)
  univer.registerPlugin(UniverFindReplacePlugin)

  // ✅ Create workbook after all plugins loaded
  univer.createUnit(Univer.SHEET, {
    name: 'Untitled Spreadsheet',
  })
})



</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: hidden;
}
</style>
