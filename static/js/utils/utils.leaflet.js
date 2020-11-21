/* exported setCustomTileServers, setTileLayer */

const tileLayers = {
    //mapnik: L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' }),
    //topomap: L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', { maxZoom: 17, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' }),
    cartodbdarkmatter: L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>' }),
    cartodbdarkmatternolabels: L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>' }),
    cartodbpositron: L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/light_all/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>' }),
    cartodbpositronnolabels: L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/light_nolabels/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>' }),
    satellite: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', { maxZoom: 20, attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community' })
}

function setCustomTileServers(tileServers) {
    for (let i = 0; i < tileServers.length; i++) {
        const key = tileServers[i][0]
        const url = tileServers[i][2]
        tileLayers[key] = L.tileLayer(url, { maxZoom: 19 })
    }
}

function setTileLayer(layerName, map) {
    // Fallback in case layername does not exist (anymore).
    if (!(layerName in tileLayers)) {
        layerName = Object.keys(tileLayers)[2]
    }

    if (map.hasLayer(tileLayers[map.tileLayerName])) {
        map.removeLayer(tileLayers[map.tileLayerName])
    }
    map.addLayer(tileLayers[layerName])
    map.tileLayerName = layerName
}

// An icon that uses <div> instead of <img>, which is measured to has way less performance overhead
L.ContentIcon = L.Icon.extend({

    createIcon: function (oldIcon) {
        return this._createDiv('icon', oldIcon)
    },

    createShadow: function (oldIcon) {
        return this._createDiv('shadow', oldIcon)
    },

    _createDiv: function (name, oldIcon) {
        const src = this._getIconUrl(name)
        if (!src) {
            return null
        }

        const div = (oldIcon && oldIcon.tagName === 'DIV') ? oldIcon : document.createElement('div')
        div.style.content = `url('${src}')`
        this._setIconStyles(div, name)
        return div
    }

})

L.contentIcon = function (options) {
    return new L.ContentIcon(options)
}
