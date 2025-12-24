---
layout: default
title: LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing
---

# LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20591" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20591v1</a>
  <a href="https://arxiv.org/pdf/2512.20591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20591v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20591v1', 'LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changyi Lin, Boda Huo, Mingyang Yu, Emily Ruppel, Bingqing Chen, Jonathan Francis, Ding Zhao

**分类**: cs.RO

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**LightTact：一种用于形变无关接触感知的视觉-触觉指尖传感器**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉触觉融合` `触觉传感器` `轻微接触感知` `光学触觉` `机器人操作`

## 📋 核心要点

1. 现有触觉传感器依赖形变来推断接触，在与液体等轻微接触场景中表现不佳，鲁棒性不足。
2. LightTact采用光学配置，阻断环境光，仅传输接触区域的漫反射光，从而直接观察接触，无需依赖形变。
3. 实验表明，LightTact能准确分割接触区域，并驱动机械臂完成水扩散等轻微接触操作，还能结合视觉-语言模型进行电阻分拣。

## 📝 摘要（中文）

本文提出了一种名为LightTact的视觉-触觉指尖传感器，用于解决轻微接触场景下的感知问题，尤其是在与液体、半液体或超软材料交互时，这些场景通常不产生宏观表面形变。LightTact基于光学原理，无需依赖形变即可直接观察接触。它采用环境光阻断的光学配置，抑制非接触区域的外部光和内部照明，仅传输真实接触处产生的漫反射光。因此，LightTact生成高对比度的原始图像，其中非接触像素保持接近黑色（平均灰度值<3），而接触像素保留接触表面的自然外观。基于此，LightTact实现了精确的像素级接触分割，对材料属性、接触力、表面外观和环境光照具有鲁棒性。该传感器被集成到机械臂上，并展示了由极轻微接触驱动的操作行为，包括水扩散、面霜蘸取和薄膜交互。此外，LightTact空间对齐的视觉-触觉图像可以直接被现有的视觉-语言模型解释，从而实现电阻值的推理，用于机器人分拣。

## 🔬 方法详解

**问题定义**：现有触觉传感器主要依赖于接触产生的形变来感知接触，这在与液体、半液体或超软材料等发生轻微接触时会失效，因为这些接触通常不会引起明显的宏观形变。因此，需要一种能够独立于形变进行接触感知的传感器。

**核心思路**：LightTact的核心思路是利用光学方法，直接“看到”接触。通过设计一种特殊的光学配置，阻断环境光和内部照明，使得只有在真实接触点产生的漫反射光才能被传感器捕捉到。这样，即使没有明显的形变，也能清晰地识别出接触区域。

**技术框架**：LightTact传感器主要由以下几个部分组成：一个指尖形状的外壳，一个用于阻断环境光的光学系统，一个内部光源（用于在接触时产生漫反射），以及一个相机。当物体与传感器接触时，内部光源发出的光会在接触表面发生漫反射，这些漫反射光穿过光学系统，被相机捕捉到。非接触区域由于环境光和内部照明被阻断，因此在图像中呈现黑色。整个流程可以概括为：环境光阻断 -> 内部照明 -> 接触表面漫反射 -> 相机成像。

**关键创新**：LightTact最重要的创新在于其形变无关的接触感知原理。与传统的触觉传感器不同，LightTact不依赖于形变来推断接触，而是直接通过光学方法观察接触。这种方法使得LightTact能够感知到非常轻微的接触，即使没有明显的形变也能准确地识别出接触区域。

**关键设计**：LightTact的关键设计在于其光学配置，需要精确地控制光路，以确保环境光和内部照明在非接触区域被有效地阻断，同时保证接触区域产生的漫反射光能够被相机捕捉到。具体的技术细节包括：光学元件的形状、位置和材料的选择，内部光源的类型和强度，以及相机的参数设置（如曝光时间和增益）。此外，图像处理算法也至关重要，需要能够有效地从原始图像中分割出接触区域。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20591v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20591v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20591v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LightTact实现了高精度的像素级接触分割，对材料属性、接触力、表面外观和环境光照具有鲁棒性。实验表明，LightTact能够驱动机械臂完成水扩散、面霜蘸取和薄膜交互等轻微接触操作。此外，LightTact与视觉-语言模型结合，实现了电阻值的推理，为机器人分拣提供了新的解决方案。

## 🎯 应用场景

LightTact在机器人操作、医疗保健、虚拟现实等领域具有广泛的应用前景。例如，在机器人操作中，它可以用于精确地控制机械臂与柔软物体的交互，如抓取易碎物品或进行精细的装配。在医疗保健领域，它可以用于开发更灵敏的医疗设备，如用于诊断或治疗的触觉传感器。在虚拟现实领域，它可以用于创建更逼真的触觉反馈，增强用户的沉浸感。

## 📄 摘要（原文）

> Contact often occurs without macroscopic surface deformation, such as during interaction with liquids, semi-liquids, or ultra-soft materials. Most existing tactile sensors rely on deformation to infer contact, making such light-contact interactions difficult to perceive robustly. To address this, we present LightTact, a visual-tactile fingertip sensor that makes contact directly visible via a deformation-independent, optics-based principle. LightTact uses an ambient-blocking optical configuration that suppresses both external light and internal illumination at non-contact regions, while transmitting only the diffuse light generated at true contacts. As a result, LightTact produces high-contrast raw images in which non-contact pixels remain near-black (mean gray value < 3) and contact pixels preserve the natural appearance of the contacting surface. Built on this, LightTact achieves accurate pixel-level contact segmentation that is robust to material properties, contact force, surface appearance, and environmental lighting. We further integrate LightTact on a robotic arm and demonstrate manipulation behaviors driven by extremely light contact, including water spreading, facial-cream dipping, and thin-film interaction. Finally, we show that LightTact's spatially aligned visual-tactile images can be directly interpreted by existing vision-language models, enabling resistor value reasoning for robotic sorting.

