---
layout: default
title: "MedFoundationHub: A Lightweight and Secure Toolkit for Deploying Medical Vision Language Foundation Models"
---

# MedFoundationHub: A Lightweight and Secure Toolkit for Deploying Medical Vision Language Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20345" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20345v1</a>
  <a href="https://arxiv.org/pdf/2508.20345.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20345v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20345v1', 'MedFoundationHub: A Lightweight and Secure Toolkit for Deploying Medical Vision Language Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Li, Yanfan Zhu, Ruining Deng, Wei-Qi Wei, Yu Wang, Shilin Zhao, Yaohong Wang, Haichun Yang, Yuankai Huo

**分类**: cs.CV, cs.HC

**发布日期**: 2025-08-28

---

## 💡 一句话要点

**提出MedFoundationHub以解决医疗视觉语言模型的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗视觉语言模型` `隐私保护` `图形用户界面` `模型部署` `Docker技术` `临床应用` `安全性`

## 📋 核心要点

1. 医疗视觉语言模型在临床应用中面临严重的安全隐患，包括PHI泄露和网络攻击风险。
2. MedFoundationHub提供了一个图形用户界面，使医生和工程师能够更安全、便捷地使用和部署医疗VLMs。
3. 通过与认证病理学家的合作，评估了五种先进VLM的性能，发现了模型在回答准确性和术语一致性方面的不足。

## 📝 摘要（中文）

近年来，医疗视觉语言模型（VLMs）的进展为临床应用带来了显著机遇，如自动报告生成和医生辅助工具。然而，医疗VLMs也引发了严重的安全隐患，尤其是在医院环境中，涉及受保护健康信息（PHI）泄露和网络威胁。为应对这些挑战，本文提出了MedFoundationHub，一个图形用户界面工具包，旨在使医生能够无编程经验地选择和使用不同模型，同时支持工程师高效部署医疗VLMs，并确保隐私保护的推理。该工具包仅需一台配备单个NVIDIA A6000 GPU的离线本地工作站，确保安全性和可访问性。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗视觉语言模型在临床应用中的安全性和易用性问题。现有方法在保护患者隐私和防止数据泄露方面存在显著不足。

**核心思路**：MedFoundationHub通过提供图形用户界面，使医生无需编程知识即可选择和使用不同的模型，同时支持工程师以即插即用的方式高效部署模型，确保隐私保护。

**技术框架**：该工具包的整体架构包括用户界面模块、模型选择模块、部署模块和隐私保护模块。用户可以通过界面选择模型，系统自动处理模型的部署和推理。

**关键创新**：MedFoundationHub的主要创新在于其图形用户界面和Docker编排的隐私保护推理方式，使得医疗VLMs的使用更加安全和便捷，显著降低了对技术背景的要求。

**关键设计**：工具包设计中采用了Docker容器技术，确保模型部署的操作系统无关性，并且只需一台配备NVIDIA A6000 GPU的本地工作站即可运行，降低了硬件要求。

## 📊 实验亮点

在与认证病理学家的合作中，评估了五种先进的医疗VLM，进行1015次评分事件。评估结果显示，模型在回答准确性、推理清晰度和病理术语一致性方面存在明显不足，提示未来改进的方向。

## 🎯 应用场景

MedFoundationHub的潜在应用领域包括医院、研究机构和医疗教育等。其安全性和易用性使得医疗专业人员能够更好地利用视觉语言模型进行临床决策支持、教育培训和研究，推动医疗技术的进步。

## 📄 摘要（原文）

> Recent advances in medical vision-language models (VLMs) open up remarkable opportunities for clinical applications such as automated report generation, copilots for physicians, and uncertainty quantification. However, despite their promise, medical VLMs introduce serious security concerns, most notably risks of Protected Health Information (PHI) exposure, data leakage, and vulnerability to cyberthreats - which are especially critical in hospital environments. Even when adopted for research or non-clinical purposes, healthcare organizations must exercise caution and implement safeguards. To address these challenges, we present MedFoundationHub, a graphical user interface (GUI) toolkit that: (1) enables physicians to manually select and use different models without programming expertise, (2) supports engineers in efficiently deploying medical VLMs in a plug-and-play fashion, with seamless integration of Hugging Face open-source models, and (3) ensures privacy-preserving inference through Docker-orchestrated, operating system agnostic deployment. MedFoundationHub requires only an offline local workstation equipped with a single NVIDIA A6000 GPU, making it both secure and accessible within the typical resources of academic research labs. To evaluate current capabilities, we engaged board-certified pathologists to deploy and assess five state-of-the-art VLMs (Google-MedGemma3-4B, Qwen2-VL-7B-Instruct, Qwen2.5-VL-7B-Instruct, and LLaVA-1.5-7B/13B). Expert evaluation covered colon cases and renal cases, yielding 1015 clinician-model scoring events. These assessments revealed recurring limitations, including off-target answers, vague reasoning, and inconsistent pathology terminology.

