---
layout: default
title: "VLH: Vision-Language-Haptics Foundation Model"
---

# VLH: Vision-Language-Haptics Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01361" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01361v1</a>
  <a href="https://arxiv.org/pdf/2508.01361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01361v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01361v1', 'VLH: Vision-Language-Haptics Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luis Francisco Moreno Fuentes, Muhammad Haris Khan, Miguel Altamirano Cabrera, Valerii Serpiva, Dmitri Iarchuk, Yara Mahmoud, Issatay Tokmurziyev, Dzmitry Tsetserukou

**分类**: cs.RO

**发布日期**: 2025-08-02

---

## 💡 一句话要点

**提出VLH模型以实现视觉、语言与触觉的统一交互**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-触觉` `人机交互` `多模态融合` `空中机器人` `虚拟现实`

## 📋 核心要点

1. 现有方法通常将触觉反馈视为次要通道，未能有效整合视觉和语言信息，导致人机交互的局限性。
2. VLH模型通过将视觉理解与自然语言指令相结合，直接生成触觉反馈，提升了人机交互的沉浸感和表达能力。
3. 在90次人机交互实验中，VLH实现了56.7%的目标获取成功率和100%的纹理辨别准确率，显示出良好的泛化能力。

## 📝 摘要（中文）

我们提出了VLH，一个新颖的视觉-语言-触觉基础模型，旨在统一空中机器人和虚拟现实中的感知、语言和触觉反馈。与以往将触觉视为次要反应通道的研究不同，VLH将空中力和振动线索作为上下文视觉理解和自然语言指令的直接结果进行合成。该平台由一架配备双逆五杆连杆阵列的8英寸四旋翼无人机、一个自我中心的虚拟现实摄像头和一个外部俯视视角组成。通过对450个多模态场景的定制数据集进行LoRA适配，使用微调的OpenVLA骨干网络处理视觉输入和语言指令，输出7维动作向量。实验结果显示，VLH在目标获取中取得了56.7%的成功率，并在纹理辨别中达到了100%的准确率，展示了其在增强人机交互中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有空中机器人和虚拟现实中触觉反馈与视觉、语言信息整合不足的问题。现有方法往往将触觉视为次要反应通道，限制了人机交互的表现力和沉浸感。

**核心思路**：VLH模型的核心思想是将视觉理解与自然语言指令结合，通过合成上下文相关的触觉反馈，提升人机交互的自然性和有效性。该设计使得触觉反馈不仅是反应，而是主动生成的结果。

**技术框架**：VLH的整体架构包括一个8英寸的四旋翼无人机，配备双逆五杆连杆阵列用于局部触觉激励，一个自我中心的虚拟现实摄像头，以及一个外部俯视视角。视觉输入和语言指令通过微调的OpenVLA骨干网络处理，输出7维动作向量。

**关键创新**：VLH的主要创新在于将触觉反馈与视觉和语言信息的理解紧密结合，形成一个统一的多模态交互系统。这一设计与传统方法的本质区别在于触觉反馈的主动生成，而非被动反应。

**关键设计**：在技术细节上，使用LoRA对定制数据集进行适配，确保模型能够处理450个多模态场景。通过INT8量化和高性能服务器，确保模型在4-5 Hz的实时操作能力。

## 📊 实验亮点

在90次人机交互实验中，VLH模型实现了56.7%的目标获取成功率，平均到达时间为21.3秒，姿态误差为0.24米。同时，在纹理辨别任务中，模型达到了100%的准确率，展示了其在多模态任务中的强大能力和可靠性。

## 🎯 应用场景

VLH模型在空中机器人和虚拟现实领域具有广泛的应用潜力。它可以用于增强现实、远程操控、教育培训等场景，提升用户体验和交互质量。未来，该模型的技术可以扩展到其他领域，如医疗、娱乐和智能家居等，推动人机交互的进一步发展。

## 📄 摘要（原文）

> We present VLH, a novel Visual-Language-Haptic Foundation Model that unifies perception, language, and tactile feedback in aerial robotics and virtual reality. Unlike prior work that treats haptics as a secondary, reactive channel, VLH synthesizes mid-air force and vibration cues as a direct consequence of contextual visual understanding and natural language commands. Our platform comprises an 8-inch quadcopter equipped with dual inverse five-bar linkage arrays for localized haptic actuation, an egocentric VR camera, and an exocentric top-down view. Visual inputs and language instructions are processed by a fine-tuned OpenVLA backbone - adapted via LoRA on a bespoke dataset of 450 multimodal scenarios - to output a 7-dimensional action vector (Vx, Vy, Vz, Hx, Hy, Hz, Hv). INT8 quantization and a high-performance server ensure real-time operation at 4-5 Hz. In human-robot interaction experiments (90 flights), VLH achieved a 56.7% success rate for target acquisition (mean reach time 21.3 s, pose error 0.24 m) and 100% accuracy in texture discrimination. Generalization tests yielded 70.0% (visual), 54.4% (motion), 40.0% (physical), and 35.0% (semantic) performance on novel tasks. These results demonstrate VLH's ability to co-evolve haptic feedback with perceptual reasoning and intent, advancing expressive, immersive human-robot interactions.

