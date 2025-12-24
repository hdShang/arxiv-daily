---
layout: default
title: "Multimodal Mathematical Reasoning Embedded in Aerial Vehicle Imagery: Benchmarking, Analysis, and Exploration"
---

# Multimodal Mathematical Reasoning Embedded in Aerial Vehicle Imagery: Benchmarking, Analysis, and Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10059" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10059v1</a>
  <a href="https://arxiv.org/pdf/2509.10059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10059v1', 'Multimodal Mathematical Reasoning Embedded in Aerial Vehicle Imagery: Benchmarking, Analysis, and Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Zhou, Litong Feng, Mengcheng Lan, Xue Yang, Qingyun Li, Yiping Ke, Xue Jiang, Wayne Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-12

**备注**: 17 pages, 16 figures

**🔗 代码/项目**: [GITHUB](https://github.com/VisionXLab/avi-math)

---

## 💡 一句话要点

**提出AVI-Math无人机图像数学推理基准，揭示现有VLM的局限性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机图像` `数学推理` `视觉语言模型` `多模态学习` `基准数据集`

## 📋 核心要点

1. 现有视觉语言模型在无人机图像的数学推理能力上缺乏充分测试，无法满足无人机遥感任务的需求。
2. 提出AVI-Math基准，包含高质量无人机图像和复杂的数学问题，用于评估和提升VLM在此领域的推理能力。
3. 实验表明现有VLM在AVI-Math上表现不佳，通过思维链提示和微调等方法，有望提升模型性能。

## 📝 摘要（中文）

本文提出了AVI-Math，这是首个严格评估无人机图像中多模态数学推理能力的基准。该基准旨在填补现有视觉语言模型（VLM）在无人机遥感领域，特别是精确距离、面积计算、轨迹估计和空间分析等任务中能力评估的空白。AVI-Math包含3773个高质量的、与无人机拍摄的车辆相关的数学问题，涵盖几何、逻辑和代数等6个数学科目和20个主题。数据在不同的高度和无人机角度下采集，反映了真实的无人机场景，保证了所构建数学问题的多样性和复杂性。通过对14个主流VLM的全面评估，结果表明这些模型在AVI-Math的推理任务中表现不佳。进一步的分析揭示了当前VLM在数学推理能力方面的显著局限性，并为未来的研究提供了方向。此外，本文还探索了思维链提示和微调技术，这些技术在解决AVI-Math中的推理挑战方面显示出潜力。代码和数据集将在https://github.com/VisionXLab/avi-math发布。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型（VLM）在无人机（UAV）图像理解中进行复杂数学推理能力不足的问题。现有VLM在通用多模态任务上取得了进展，但在特定领域，如无人机遥感图像的分析，尤其是在需要几何、逻辑和代数等数学知识进行推理的任务中，表现出明显的局限性。现有的数据集和基准测试主要集中在简单的计数任务，无法充分评估VLM在复杂场景下的数学推理能力。

**核心思路**：论文的核心思路是构建一个专门针对无人机图像的数学推理基准数据集AVI-Math，该数据集包含多样化的数学问题，涵盖几何、逻辑和代数等多个领域，并且问题与无人机拍摄的真实场景紧密结合。通过在该数据集上评估现有VLM的性能，可以揭示其在数学推理方面的不足，并为未来的研究提供方向。此外，论文还探索了思维链（Chain-of-Thought）提示和微调等技术，以提升VLM在AVI-Math上的性能。

**技术框架**：整体框架包括数据集构建和模型评估两部分。数据集构建涉及从不同高度和角度采集无人机图像，并根据图像内容设计相应的数学问题。这些问题涵盖不同的数学科目和主题，旨在测试VLM在不同场景下的推理能力。模型评估部分则选取了14个主流VLM，并在AVI-Math数据集上进行测试，分析其在不同类型问题上的表现。此外，还探索了思维链提示和微调等技术，以提升VLM的性能。

**关键创新**：论文的关键创新在于构建了首个针对无人机图像的数学推理基准数据集AVI-Math。与现有数据集相比，AVI-Math更加关注复杂场景下的数学推理能力，并且问题与无人机拍摄的真实场景紧密结合。此外，论文还对现有VLM在AVI-Math上的性能进行了全面评估，揭示了其在数学推理方面的不足，并为未来的研究提供了方向。

**关键设计**：AVI-Math数据集包含3773个高质量的、与无人机拍摄的车辆相关的数学问题，涵盖几何、逻辑和代数等6个数学科目和20个主题。数据在不同的高度和无人机角度下采集，反映了真实的无人机场景。在模型评估方面，论文选取了14个主流VLM，并采用了思维链提示和微调等技术来提升模型性能。具体的参数设置和网络结构等技术细节在论文中没有详细描述，可能需要参考相关模型的原始论文。

## 📊 实验亮点

实验结果表明，现有主流VLM在AVI-Math数据集上的表现不佳，表明其在无人机图像的数学推理能力方面存在显著局限性。通过采用思维链提示和微调等技术，VLM在AVI-Math上的性能得到了一定的提升，但仍有很大的改进空间。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于无人机遥感图像的智能分析，例如精确的距离和面积计算、轨迹估计、空间分析等。在智慧城市、农业监测、灾害评估等领域具有广泛的应用前景。通过提升VLM在无人机图像上的数学推理能力，可以实现更智能、更高效的无人机应用。

## 📄 摘要（原文）

> Mathematical reasoning is critical for tasks such as precise distance and area computations, trajectory estimations, and spatial analysis in unmanned aerial vehicle (UAV) based remote sensing, yet current vision-language models (VLMs) have not been adequately tested in this domain. To address this gap, we introduce AVI-Math, the first benchmark to rigorously evaluate multimodal mathematical reasoning in aerial vehicle imagery, moving beyond simple counting tasks to include domain-specific knowledge in areas such as geometry, logic, and algebra. The dataset comprises 3,773 high-quality vehicle-related questions captured from UAV views, covering 6 mathematical subjects and 20 topics. The data, collected at varying altitudes and from multiple UAV angles, reflects real-world UAV scenarios, ensuring the diversity and complexity of the constructed mathematical problems. In this paper, we benchmark 14 prominent VLMs through a comprehensive evaluation and demonstrate that, despite their success on previous multimodal benchmarks, these models struggle with the reasoning tasks in AVI-Math. Our detailed analysis highlights significant limitations in the mathematical reasoning capabilities of current VLMs and suggests avenues for future research. Furthermore, we explore the use of Chain-of-Thought prompting and fine-tuning techniques, which show promise in addressing the reasoning challenges in AVI-Math. Our findings not only expose the limitations of VLMs in mathematical reasoning but also offer valuable insights for advancing UAV-based trustworthy VLMs in real-world applications. The code, and datasets will be released at https://github.com/VisionXLab/avi-math

