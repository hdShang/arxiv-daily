---
layout: default
title: mmWalk: Towards Multi-modal Multi-view Walking Assistance
---

# mmWalk: Towards Multi-modal Multi-view Walking Assistance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11520" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11520v2</a>
  <a href="https://arxiv.org/pdf/2510.11520.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11520v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11520v2', 'mmWalk: Towards Multi-modal Multi-view Walking Assistance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kedi Ying, Ruiping Liu, Chongyan Chen, Mingzhe Tao, Hao Shi, Kailun Yang, Jiaming Zhang, Rainer Stiefelhagen

**分类**: cs.CV

**发布日期**: 2025-10-13 (更新: 2025-10-23)

**备注**: Accepted by NeurIPS 2025 Datasets and Benchmarks Track. Data and Code: https://github.com/KediYing/mmWalk

---

## 💡 一句话要点

**mmWalk：面向盲人或低视力人群的多模态多视角步行辅助数据集与方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多模态学习` `步行辅助` `视觉障碍` `数据集构建` `视觉问答`

## 📋 核心要点

1. 现有方法在理解复杂环境方面存在不足，难以有效辅助盲人或低视力人群在户外安全行走。
2. mmWalk数据集通过集成多视角传感器数据和可访问性特征，模拟真实世界场景，为步行辅助提供更全面的信息。
3. 实验表明，在mmWalk上微调的模型在真实世界数据集中表现良好，验证了数据集的有效性。

## 📝 摘要（中文）

本文针对盲人或低视力(BLV)人群在极端或复杂环境中行走辅助的挑战，构建了一个名为mmWalk的模拟多模态数据集，该数据集集成了多视角传感器和面向可访问性的特征，用于户外安全导航。mmWalk包含120条手动控制、场景分类的行走轨迹，共计62k同步帧，超过559k张RGB、深度和语义模态的全景图像。为了强调真实世界的关联性，每条轨迹都包含户外极端情况和BLV用户的可访问性特定地标。此外，本文还生成了mmWalkVQA，一个包含超过69k个视觉问答三元组的VQA基准，涵盖9个类别，专为安全和知情的步行辅助而定制。通过零样本和少样本设置评估了最先进的视觉语言模型(VLM)，发现它们在风险评估和导航任务中表现不佳。最后，在真实世界数据集上验证了mmWalk微调模型的有效性，证明了该数据集在推进多模态步行辅助方面的价值。

## 🔬 方法详解

**问题定义**：现有步行辅助系统缺乏对复杂环境的全面理解，尤其是在极端或复杂场景下，无法为盲人或低视力人群提供充分的安全保障。现有方法难以有效整合多模态信息，并缺乏针对BLV用户的特定场景和地标的考虑。

**核心思路**：本文的核心思路是构建一个包含多模态信息（RGB、深度、语义）和针对BLV用户的特定场景和地标的模拟数据集mmWalk，从而训练更有效的步行辅助模型。通过模拟真实世界的复杂场景，使模型能够更好地理解和应对实际挑战。

**技术框架**：mmWalk数据集包含120条手动控制的行走轨迹，每条轨迹包含同步的RGB、深度和语义图像。此外，还构建了mmWalkVQA基准，用于评估模型在视觉问答方面的能力。整体流程包括数据采集、场景分类、数据标注（包括语义分割和VQA标注）以及模型训练和评估。

**关键创新**：关键创新在于数据集的设计，它不仅包含多模态信息，还特别关注了BLV用户的需求，例如，包含了可访问性特定地标和户外极端情况。此外，mmWalkVQA基准的构建也为评估模型在步行辅助方面的能力提供了一个新的平台。

**关键设计**：数据集包含62k同步帧，超过559k张全景图像。mmWalkVQA包含超过69k个视觉问答三元组，涵盖9个类别，例如“是否存在障碍物？”、“行人道是否畅通？”等。在模型训练方面，使用了标准的视觉语言模型，并在mmWalk数据集上进行了微调。

## 📊 实验亮点

实验结果表明，在mmWalk数据集上微调的视觉语言模型在真实世界数据集上表现出显著的性能提升，验证了mmWalk数据集的有效性。具体而言，在风险评估和导航任务中，微调后的模型相比于零样本和少样本学习方法，取得了明显的性能提升。这些结果表明，mmWalk数据集能够有效地提升模型在多模态步行辅助方面的能力。

## 🎯 应用场景

该研究成果可应用于开发更智能、更安全的步行辅助系统，帮助盲人或低视力人群在户外环境中独立行走。通过结合多模态传感器信息和可访问性特征，可以提高步行辅助系统的环境感知能力和风险评估能力，从而提升BLV用户的出行体验和生活质量。未来，该技术还可以扩展到其他辅助机器人领域，例如老年人辅助和残疾人辅助。

## 📄 摘要（原文）

> Walking assistance in extreme or complex environments remains a significant challenge for people with blindness or low vision (BLV), largely due to the lack of a holistic scene understanding. Motivated by the real-world needs of the BLV community, we build mmWalk, a simulated multi-modal dataset that integrates multi-view sensor and accessibility-oriented features for outdoor safe navigation. Our dataset comprises 120 manually controlled, scenario-categorized walking trajectories with 62k synchronized frames. It contains over 559k panoramic images across RGB, depth, and semantic modalities. Furthermore, to emphasize real-world relevance, each trajectory involves outdoor corner cases and accessibility-specific landmarks for BLV users. Additionally, we generate mmWalkVQA, a VQA benchmark with over 69k visual question-answer triplets across 9 categories tailored for safe and informed walking assistance. We evaluate state-of-the-art Vision-Language Models (VLMs) using zero- and few-shot settings and found they struggle with our risk assessment and navigational tasks. We validate our mmWalk-finetuned model on real-world datasets and show the effectiveness of our dataset for advancing multi-modal walking assistance.

