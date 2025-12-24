---
layout: default
title: "PalpAid: Multimodal Pneumatic Tactile Sensor for Tissue Palpation"
---

# PalpAid: Multimodal Pneumatic Tactile Sensor for Tissue Palpation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19010" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19010v1</a>
  <a href="https://arxiv.org/pdf/2512.19010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19010v1', 'PalpAid: Multimodal Pneumatic Tactile Sensor for Tissue Palpation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Devi Yuliarti, Ravi Prakash, Hiu Ching Cheung, Amy Strong, Patrick J. Codd, Shan Lin

**分类**: eess.SP, cs.RO

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**PalpAid：用于组织触诊的多模态气动触觉传感器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `触觉传感器` `气动触觉` `多模态感知` `机器人辅助手术` `组织触诊`

## 📋 核心要点

1. 机器人辅助手术中，外科医生缺乏触觉反馈，影响肿瘤边界的精确识别。
2. PalpAid采用气动原理，通过压力传感器和麦克风感知接触力和声音，实现多模态触觉感知。
3. 实验验证了PalpAid的鲁棒性，并展示了其在区分不同硬度物体和组织方面的能力。

## 📝 摘要（中文）

在外科肿瘤学中，组织的触觉特性（如弹性和硬度）在识别肿瘤和病理组织边界方面起着重要作用。机器人辅助手术虽然极具价值，但也降低了外科医生的感觉信息，通常只有视觉可用。为了克服这种感觉缺失，提出的传感器通常体积庞大、结构复杂且与手术流程不兼容。本文提出了一种多模态气动触觉传感器PalpAid，配备麦克风和压力传感器，将接触力转换为内部压差。压力传感器用作事件检测器，而麦克风捕获的听觉特征有助于组织划界。本文展示了传感单元的设计、制造和组装，并通过特性测试证明了其耐用性、充放气循环能力以及与机器人系统的集成能力。最后，本文展示了该传感器对具有不同填充密度的3D打印硬物和离体软组织的分类能力。总而言之，PalpAid旨在智能地填补感觉空白，并改进临床决策。

## 🔬 方法详解

**问题定义**：机器人辅助手术中，外科医生依赖视觉信息，缺乏触觉反馈，难以准确识别肿瘤边界和组织特性。现有的触觉传感器通常体积大、结构复杂，难以集成到手术流程中，且成本较高。

**核心思路**：PalpAid的核心思路是利用气动原理，将接触力转换为内部压差，并通过压力传感器和麦克风分别感知压力变化和声音信号。通过融合压力和声音信息，实现对组织特性的多模态感知，从而辅助外科医生进行更精确的触诊。

**技术框架**：PalpAid系统主要由以下几个部分组成：1) 气动触觉传感单元：包含一个气囊、一个压力传感器和一个麦克风。气囊与组织接触时，压力变化被压力传感器捕捉，同时麦克风记录接触产生的声音。2) 信号处理单元：对压力传感器和麦克风采集到的信号进行处理，提取特征。3) 分类算法：利用机器学习算法，根据提取的特征对组织类型进行分类。

**关键创新**：PalpAid的关键创新在于：1) 采用气动原理，结构简单、体积小，易于集成到机器人手术系统中。2) 融合压力和声音信息，实现多模态触觉感知，提高了组织识别的准确性。3) 使用低成本的压力传感器和麦克风，降低了传感器的成本。

**关键设计**：气囊的材料和尺寸是关键设计参数，需要根据应用场景进行优化。压力传感器的量程和精度需要满足触诊的需求。麦克风的灵敏度和频率响应范围需要能够捕捉到组织接触产生的声音信号。分类算法的选择需要根据数据集的特点进行调整，常用的算法包括支持向量机（SVM）和神经网络。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19010v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19010v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19010v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PalpAid能够有效区分不同硬度的3D打印物体和离体软组织。通过压力和声音信号的融合，PalpAid在组织分类任务中取得了较高的准确率，证明了其在触觉感知方面的潜力。该传感器具有良好的鲁棒性，能够承受多次充放气循环，并能与机器人系统集成。

## 🎯 应用场景

PalpAid可应用于机器人辅助手术中，为外科医生提供触觉反馈，辅助肿瘤边界识别和组织特性判断，提高手术精度和成功率。此外，该技术还可应用于远程医疗、康复机器人等领域，实现远程触诊和个性化康复治疗。未来，结合人工智能技术，PalpAid有望实现更智能化的触觉感知和诊断。

## 📄 摘要（原文）

> The tactile properties of tissue, such as elasticity and stiffness, often play an important role in surgical oncology when identifying tumors and pathological tissue boundaries. Though extremely valuable, robot-assisted surgery comes at the cost of reduced sensory information to the surgeon; typically, only vision is available. Sensors proposed to overcome this sensory desert are often bulky, complex, and incompatible with the surgical workflow. We present PalpAid, a multimodal pneumatic tactile sensor equipped with a microphone and pressure sensor, converting contact force into an internal pressure differential. The pressure sensor acts as an event detector, while the auditory signature captured by the microphone assists in tissue delineation. We show the design, fabrication, and assembly of sensory units with characterization tests to show robustness to use, inflation-deflation cycles, and integration with a robotic system. Finally, we show the sensor's ability to classify 3D-printed hard objects with varying infills and soft ex vivo tissues. Overall, PalpAid aims to fill the sensory gap intelligently and allow improved clinical decision-making.

