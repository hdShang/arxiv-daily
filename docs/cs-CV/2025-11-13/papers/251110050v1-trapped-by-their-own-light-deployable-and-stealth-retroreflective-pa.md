---
layout: default
title: Trapped by Their Own Light: Deployable and Stealth Retroreflective Patch Attacks on Traffic Sign Recognition Systems
---

# Trapped by Their Own Light: Deployable and Stealth Retroreflective Patch Attacks on Traffic Sign Recognition Systems

**arXiv**: [2511.10050v1](https://arxiv.org/abs/2511.10050) | [PDF](https://arxiv.org/pdf/2511.10050.pdf)

**作者**: Go Tsuruoka, Takami Sato, Qi Alfred Chen, Kazuki Nomoto, Ryunosuke Kobayashi, Yuna Tanaka, Tatsuya Mori

---

## 💡 一句话要点

**提出可部署隐形的逆向反射补丁攻击，针对交通标志识别系统。**

**关键词**: `交通标志识别` `逆向反射攻击` `黑盒优化` `隐形补丁` `防御方法` `自动驾驶安全`

## 📋 核心要点

1. 交通标志识别系统易受攻击，现有方法视觉可检测或实现受限。
2. 利用逆向反射材料，仅在车灯照射下激活，结合黑盒优化提升攻击效果。
3. 动态场景成功率≥93.4%，真实世界≥60%，用户研究显示隐形性优于先前攻击。

## 📄 摘要（原文）

> Traffic sign recognition plays a critical role in ensuring safe and efficient transportation of autonomous vehicles but remain vulnerable to adversarial attacks using stickers or laser projections. While existing attack vectors demonstrate security concerns, they suffer from visual detectability or implementation constraints, suggesting unexplored vulnerability surfaces in TSR systems. We introduce the Adversarial Retroreflective Patch (ARP), a novel attack vector that combines the high deployability of patch attacks with the stealthiness of laser projections by utilizing retroreflective materials activated only under victim headlight illumination. We develop a retroreflection simulation method and employ black-box optimization to maximize attack effectiveness. ARP achieves $\geq$93.4\% success rate in dynamic scenarios at 35 meters and $\geq$60\% success rate against commercial TSR systems in real-world conditions. Our user study demonstrates that ARP attacks maintain near-identical stealthiness to benign signs while achieving $\geq$1.9\% higher stealthiness scores than previous patch attacks. We propose the DPR Shield defense, employing strategically placed polarized filters, which achieves $\geq$75\% defense success rates for stop signs and speed limit signs against micro-prism patches.

