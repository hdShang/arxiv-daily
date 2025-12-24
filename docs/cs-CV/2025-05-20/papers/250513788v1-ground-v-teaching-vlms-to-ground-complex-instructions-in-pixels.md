---
layout: default
title: "Ground-V: Teaching VLMs to Ground Complex Instructions in Pixels"
---

# Ground-V: Teaching VLMs to Ground Complex Instructions in Pixels

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13788" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13788v1</a>
  <a href="https://arxiv.org/pdf/2505.13788.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13788v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13788v1', 'Ground-V: Teaching VLMs to Ground Complex Instructions in Pixels')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongshuo Zong, Qin Zhang, Dongsheng An, Zhihua Li, Xiang Xu, Linghan Xu, Zhuowen Tu, Yifan Xing, Onkar Dabeer

**分类**: cs.CV

**发布日期**: 2025-05-20

**备注**: Accepted to CVPR'25

---

## 💡 一句话要点

**提出Ground-V以解决复杂指令的像素级定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `知识蒸馏` `像素级定位` `复杂指令` `多对象场景` `数据集生成` `自动化标注`

## 📋 核心要点

1. 现有方法在处理复杂指令时面临虚假引用、多对象场景和推理等多重挑战，导致定位精度不足。
2. 本研究通过知识蒸馏生成高质量的指令-响应对，结合现有像素级注释，减少人工标注需求。
3. 实验结果显示，基于Ground-V训练的模型在多个基准测试上取得了显著的性能提升，尤其在gRefCOCO上达到83.3%的N-Acc。

## 📝 摘要（中文）

本研究提出了一种简单而有效的工作流程，旨在自动扩展指令跟随数据，以引导视觉语言模型（VLMs）在复杂指令下实现像素级的定位能力。我们特别解决了文本指令基础定位中的五个关键现实挑战：虚假引用、多对象场景、推理、多粒度和部分引用。通过利用预训练教师模型的知识蒸馏，我们的方法生成了与现有像素级注释相关的高质量指令-响应对，最大限度地减少了对昂贵人工注释的需求。生成的数据集Ground-V捕捉了丰富的对象定位知识和细致的像素级引用表达。实验结果表明，基于Ground-V训练的模型在多种定位任务上表现出显著提升，具体而言，在LISA和PSALM的训练中，平均准确率分别提高了4.4%和7.9%。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型在复杂指令下的像素级定位问题。现有方法在处理多对象场景和推理时，常常出现虚假引用和定位不准确的情况。

**核心思路**：我们提出通过知识蒸馏从预训练教师模型中提取信息，生成高质量的指令-响应对，以此来增强模型的像素级定位能力，减少对人工注释的依赖。

**技术框架**：整体架构包括数据生成、知识蒸馏和模型训练三个主要阶段。首先，通过教师模型生成指令-响应对，然后利用这些数据进行模型训练，以提高其在复杂场景下的表现。

**关键创新**：本研究的主要创新在于通过知识蒸馏生成高质量的指令-响应对，显著提升了模型在复杂指令下的像素级定位能力。这一方法与传统的人工标注方式相比，效率更高且成本更低。

**关键设计**：在模型训练中，我们采用了特定的损失函数来优化指令与响应之间的匹配度，并设计了适合多粒度引用的网络结构，以提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，使用Ground-V训练的模型在LISA和PSALM任务上分别提高了4.4%和7.9%的准确率，并在标准基准测试如RefCOCO/+/g上设立了新的最先进结果。在gRefCOCO上，模型的N-Acc达到了83.3%，超越了之前的最先进水平超过20%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人导航等，能够帮助系统更好地理解和执行复杂的视觉指令。通过提高模型的像素级定位能力，未来可以在多种实际场景中实现更高效的交互和操作。

## 📄 摘要（原文）

> This work presents a simple yet effective workflow for automatically scaling instruction-following data to elicit pixel-level grounding capabilities of VLMs under complex instructions. In particular, we address five critical real-world challenges in text-instruction-based grounding: hallucinated references, multi-object scenarios, reasoning, multi-granularity, and part-level references. By leveraging knowledge distillation from a pre-trained teacher model, our approach generates high-quality instruction-response pairs linked to existing pixel-level annotations, minimizing the need for costly human annotation. The resulting dataset, Ground-V, captures rich object localization knowledge and nuanced pixel-level referring expressions. Experiment results show that models trained on Ground-V exhibit substantial improvements across diverse grounding tasks. Specifically, incorporating Ground-V during training directly achieves an average accuracy boost of 4.4% for LISA and a 7.9% for PSALM across six benchmarks on the gIoU metric. It also sets new state-of-the-art results on standard benchmarks such as RefCOCO/+/g. Notably, on gRefCOCO, we achieve an N-Acc of 83.3%, exceeding the previous state-of-the-art by more than 20%.

