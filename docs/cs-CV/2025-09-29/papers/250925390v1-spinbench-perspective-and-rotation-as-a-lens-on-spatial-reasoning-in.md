---
layout: default
title: "SpinBench: Perspective and Rotation as a Lens on Spatial Reasoning in VLMs"
---

# SpinBench: Perspective and Rotation as a Lens on Spatial Reasoning in VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25390" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25390v1</a>
  <a href="https://arxiv.org/pdf/2509.25390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25390v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25390v1', 'SpinBench: Perspective and Rotation as a Lens on Spatial Reasoning in VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyou Zhang, Radu Corcodel, Chiori Hori, Anoop Cherian, Ding Zhao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-29

**🔗 代码/项目**: [PROJECT_PAGE](https://spinbench25.github.io/)

---

## 💡 一句话要点

**提出SpinBench以评估视觉语言模型的空间推理能力**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `空间推理` `视觉语言模型` `视角转换` `认知基准` `多模态评估` `模型评估` `任务设计`

## 📋 核心要点

1. 现有视觉语言模型在空间推理方面存在系统性弱点，特别是在视角转换和物体关系理解上。
2. SpinBench通过引入细致的诊断类别，系统评估模型在空间推理中的表现，特别关注视角变化的影响。
3. 实验结果显示，VLMs在空间推理任务中表现不佳，且与人类的反应时间和准确率存在显著相关性。

## 📝 摘要（中文）

我们提出了SpinBench，这是一个基于认知的诊断基准，用于评估视觉语言模型（VLMs）中的空间推理能力。SpinBench围绕空间推理的核心挑战——视角转换而设计，要求模型能够理解场景和物体关系在视点变化下的变化。由于视角转换需要多种认知能力，如跨视图识别物体、相对位置的基础以及心理模拟变换，SpinBench引入了一系列细致的诊断类别，涵盖平移、旋转、物体相对姿态和视点变化等。我们评估了37个最先进的VLMs，结果揭示了系统性的弱点，如强烈的自我中心偏见、旋转理解能力差以及在对称和句法重构下的不一致性。人类受试者的高准确率（91.2%）与VLM的准确率呈强相关，表明SpinBench捕捉了人类和VLMs共享的空间推理挑战。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型在空间推理，尤其是视角转换方面的不足。现有方法未能有效捕捉物体关系在不同视角下的变化，导致推理能力受限。

**核心思路**：SpinBench的核心思路是通过引入多层次的诊断任务，逐步增加任务难度，从单一物体的简单任务到多物体的复杂视角推理，全面评估模型的空间推理能力。

**技术框架**：SpinBench的整体架构包括多个模块，首先是任务设计模块，定义不同的空间推理任务；其次是评估模块，针对37个VLMs进行系统评估；最后是结果分析模块，分析模型的表现和潜在弱点。

**关键创新**：SpinBench的最大创新在于其细致的任务分类和逐步增加的难度设计，使得模型在空间推理能力的评估上更加全面和系统。与现有方法相比，SpinBench能够更好地捕捉模型在不同视角下的表现差异。

**关键设计**：在设计上，SpinBench采用了多种任务类型，包括平移、旋转和相对姿态等，使用了精确的评估标准来量化模型的表现，确保评估结果的可靠性和有效性。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，37个VLMs在SpinBench测试中表现出明显的自我中心偏见和旋转理解能力不足。人类受试者的准确率达到91.2%，而VLMs的表现与人类的反应时间呈现出强相关性，表明SpinBench有效捕捉了空间推理的挑战。

## 🎯 应用场景

SpinBench的研究成果可广泛应用于视觉语言模型的开发与优化，尤其是在需要空间推理能力的任务中，如自动驾驶、机器人导航和增强现实等领域。通过提升模型的空间理解能力，可以显著改善其在复杂环境中的表现，推动相关技术的进步与应用。

## 📄 摘要（原文）

> We present SpinBench, a cognitively grounded diagnostic benchmark for evaluating spatial reasoning in vision language models (VLMs). SpinBench is designed around the core challenge of spatial reasoning: perspective taking, the ability to reason about how scenes and object relations change under viewpoint transformation. Since perspective taking requires multiple cognitive capabilities, such as recognizing objects across views, relative positions grounding, and mentally simulating transformations, SpinBench introduces a set of fine-grained diagnostic categories. Our categories target translation, rotation, object relative pose, and viewpoint change, and are progressively structured so that single-object simpler tasks scaffold toward the most demanding multi-object perspective-taking setting. We evaluate 37 state-of-the-art VLMs, both proprietary and open source. Results reveal systematic weaknesses: strong egocentric bias, poor rotational understanding, and inconsistencies under symmetrical and syntactic reformulations. Scaling analysis shows both smooth improvements and emergent capabilities. While human subjects achieve high accuracy (91.2\%), task difficulty as measured by human response time shows strong correlation with VLM accuracy, indicating that SpinBench captures spatial reasoning challenges shared across humans and VLMs. We believe SpinBench provides critical insights into spatial reasoning in VLMs and highlights key gaps in their ability to reason about physical space. Our website can be found at https://spinbench25.github.io/.

