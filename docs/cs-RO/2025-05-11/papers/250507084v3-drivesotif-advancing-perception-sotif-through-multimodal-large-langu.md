---
layout: default
title: "DriveSOTIF: Advancing Perception SOTIF Through Multimodal Large Language Models"
---

# DriveSOTIF: Advancing Perception SOTIF Through Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07084" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07084v3</a>
  <a href="https://arxiv.org/pdf/2505.07084.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07084v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07084v3', 'DriveSOTIF: Advancing Perception SOTIF Through Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shucheng Huang, Freda Shi, Chen Sun, Jiaming Zhong, Minghao Ning, Yufeng Yang, Yukun Lu, Hong Wang, Amir Khajepour

**分类**: cs.RO

**发布日期**: 2025-05-11 (更新: 2025-09-09)

**备注**: This work has been accepted to IEEE Transactions on Vehicular Technology. Please refer to the copyright notice for additional information

**DOI**: [10.1109/TVT.2025.3608811](https://doi.org/10.1109/TVT.2025.3608811)

---

## 💡 一句话要点

**提出DriveSOTIF以解决自动驾驶中的感知安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `意图功能安全` `自动驾驶` `感知能力` `视觉问答` `模型微调` `安全风险识别`

## 📋 核心要点

1. 现有自动驾驶系统在复杂驾驶环境中缺乏人类驾驶员的感知和反应能力，导致SOTIF风险管理困难。
2. 本文提出通过微调多模态大型语言模型，利用定制数据集捕捉感知相关的SOTIF场景，以提升自动驾驶的安全性。
3. 实验结果表明，微调后的模型在视觉问答任务上显著提升，准确率分别提高11.8%和12.0%，且保持实时性能。

## 📝 摘要（中文）

人类驾驶员具备空间和因果智能，能够感知驾驶场景、预判危险并对动态环境作出反应。然而，现有的自动驾驶车辆在这些能力上存在不足，尤其是在复杂或不可预测的驾驶条件下，难以管理与感知相关的意图功能安全（SOTIF）风险。为此，本文提出了一种通过对多模态大型语言模型（MLLMs）进行微调的方法，利用专门设计的数据集捕捉感知相关的SOTIF场景。基准测试结果显示，微调后的MLLMs在封闭式视觉问答（VQA）准确率上提高了11.8%，开放式VQA得分提高了12.0%，同时保持了每张图像平均0.59秒的实时推理性能。通过在加拿大和中国的实际案例研究验证了该方法的有效性，微调模型能够正确识别即使是经验丰富的人类驾驶员也面临的安全风险。这项工作是领域特定的MLLM微调在自动驾驶SOTIF领域的首次应用。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶系统在复杂环境下感知能力不足的问题，现有方法在处理SOTIF风险时存在显著缺陷，尤其是在动态和不可预测的驾驶场景中。

**核心思路**：通过微调多模态大型语言模型（MLLMs），利用专门设计的数据集来捕捉和理解感知相关的SOTIF场景，从而增强自动驾驶系统的感知和决策能力。

**技术框架**：整体架构包括数据集构建、模型微调和性能评估三个主要阶段。数据集专注于感知相关的SOTIF场景，模型微调则针对这些特定场景进行优化，最后通过基准测试评估模型的性能。

**关键创新**：本文的主要创新在于首次将领域特定的MLLM微调应用于自动驾驶的SOTIF领域，显著提升了模型在复杂场景下的感知能力。

**关键设计**：在微调过程中，采用了特定的损失函数和参数设置，以确保模型能够有效学习感知相关的特征，并在实时推理中保持高效性。

## 📊 实验亮点

实验结果显示，微调后的多模态大型语言模型在封闭式视觉问答准确率上提升了11.8%，开放式视觉问答得分提高了12.0%。同时，模型保持了每张图像平均0.59秒的推理时间，展现出良好的实时性能。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和安全监控等。通过提升自动驾驶系统的感知能力，能够有效降低交通事故风险，提高行车安全性，未来可能对智能交通的普及和发展产生深远影响。

## 📄 摘要（原文）

> Human drivers possess spatial and causal intelligence, enabling them to perceive driving scenarios, anticipate hazards, and react to dynamic environments. In contrast, autonomous vehicles lack these abilities, making it challenging to manage perception-related Safety of the Intended Functionality (SOTIF) risks, especially under complex or unpredictable driving conditions. To address this gap, we propose fine-tuning multimodal large language models (MLLMs) on a customized dataset specifically designed to capture perception-related SOTIF scenarios. Benchmarking results show that fine-tuned MLLMs achieve an 11.8\% improvement in close-ended VQA accuracy and a 12.0\% increase in open-ended VQA scores compared to baseline models, while maintaining real-time performance with a 0.59-second average inference time per image. We validate our approach through real-world case studies in Canada and China, where fine-tuned models correctly identify safety risks that challenge even experienced human drivers. This work represents the first application of domain-specific MLLM fine-tuning for SOTIF domain in autonomous driving. The dataset and related resources are available at github.com/s95huang/DriveSOTIF.git

