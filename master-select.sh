#!/bin/bash

config_file="/opt/MMDVM_Bridge/MMDVM_Bridge.ini"
brandmeister_address="3103.master.brandmeister.network"
brandmeister_password="phiks420"
tgif_address="tgif.network"
tgif_password="865C023AF63F2AFB"

toggle_master() {
    if grep -q "^Address=$brandmeister_address" "$config_file"; then
        sed -i "s/^Address=$brandmeister_address/#Address=$brandmeister_address/" "$config_file"
        sed -i "s/^Password=$brandmeister_password/#Password=$brandmeister_password/" "$config_file"
        sed -i "s/^#Address=$tgif_address/Address=$tgif_address/" "$config_file"
        sed -i "s/^#Password=$tgif_password/Password=$tgif_password/" "$config_file"
    else
        sed -i "s/^Address=$tgif_address/#Address=$tgif_address/" "$config_file"
        sed -i "s/^Password=$tgif_password/#Password=$tgif_password/" "$config_file"
        sed -i "s/^#Address=$brandmeister_address/Address=$brandmeister_address/" "$config_file"
        sed -i "s/^#Password=$brandmeister_password/Password=$brandmeister_password/" "$config_file"
    fi

    systemctl restart mmdvm_bridge
}

toggle_master

