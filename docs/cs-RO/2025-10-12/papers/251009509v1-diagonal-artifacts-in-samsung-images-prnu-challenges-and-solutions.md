---
layout: default
title: Diagonal Artifacts in Samsung Images: PRNU Challenges and Solutions
---

# Diagonal Artifacts in Samsung Images: PRNU Challenges and Solutions

**arXiv**: [2510.09509v1](https://arxiv.org/abs/2510.09509) | [PDF](https://arxiv.org/pdf/2510.09509.pdf)

**作者**: David Vázquez-Padín, Fernando Pérez-González, Alejandro Martín-Del-Río

---

## 💡 一句话要点

**分析三星图像对角线伪影对PRNU验证的影响并提出解决方案**

**关键词**: `图像伪影分析` `PRNU相机验证` `原始图像处理` `法医图像应用` `智能手机成像`

## 📋 核心要点

1. 三星Galaxy S和A系列图像存在对角线伪影，导致PRNU指纹碰撞问题
2. 使用PRO模式原始图像可避免伪影，但中端A系列和法医场景无法应用
3. 伪影可用于减少HDR误检和定位肖像模式合成虚化区域

## 📄 摘要（原文）

> We investigate diagonal artifacts present in images captured by several
> Samsung smartphones and their impact on PRNU-based camera source verification.
> We first show that certain Galaxy S series models share a common pattern
> causing fingerprint collisions, with a similar issue also found in some Galaxy
> A models. Next, we demonstrate that reliable PRNU verification remains feasible
> for devices supporting PRO mode with raw capture, since raw images bypass the
> processing pipeline that introduces artifacts. This option, however, is not
> available for the mid-range A series models or in forensic cases without access
> to raw images. Finally, we outline potential forensic applications of the
> diagonal artifacts, such as reducing misdetections in HDR images and localizing
> regions affected by synthetic bokeh in portrait-mode images.

