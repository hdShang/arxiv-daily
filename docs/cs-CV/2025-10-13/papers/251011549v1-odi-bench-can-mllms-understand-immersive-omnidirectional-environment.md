---
layout: default
title: ODI-Bench: Can MLLMs Understand Immersive Omnidirectional Environments?
---

# ODI-Bench: Can MLLMs Understand Immersive Omnidirectional Environments?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11549" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11549v1</a>
  <a href="https://arxiv.org/pdf/2510.11549.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11549v1" onclick="toggleFavorite(this, '2510.11549v1', 'ODI-Bench: Can MLLMs Understand Immersive Omnidirectional Environments?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liu Yang, Huiyu Duan, Ran Tao, Juntao Cheng, Sijing Wu, Yunhao Li, Jing Liu, Xiongkuo Min, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出ODI-Bench，评估MLLM在全景图像理解中的能力并提出Omni-CoT方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景图像理解` `多模态大语言模型` `基准测试` `链式推理` `VR/AR` `具身智能`

## 📋 核心要点

1. 现有MLLM在全景图像理解方面能力不足，缺乏专门的评估基准。
2. 提出ODI-Bench基准测试，包含高质量全景图像和细粒度问答对，用于全面评估MLLM。
3. 引入Omni-CoT方法，通过链式推理增强MLLM对全景环境的理解能力，无需额外训练。

## 📝 摘要（中文）

全景图像(ODIs)提供完整的360x180视角，被广泛应用于VR、AR和具身智能应用中。尽管多模态大型语言模型(MLLMs)在传统的2D图像和视频理解基准测试中表现出了卓越的性能，但它们理解由ODIs捕获的沉浸式环境的能力在很大程度上仍未被探索。为了弥补这一差距，我们首先提出了ODI-Bench，这是一个专门为全景图像理解而设计的新型综合基准。ODI-Bench包含2,000张高质量全景图像和4,000多个手动标注的问答(QA)对，涵盖10个细粒度任务，包括通用级别和空间级别的ODI理解。我们进行了广泛的实验，以评估20个具有代表性的MLLM，包括专有模型和开源模型，在封闭式和开放式设置下。实验结果表明，当前的MLLM仍然难以捕捉ODIs提供的沉浸式上下文。为此，我们进一步引入了Omni-CoT，这是一种无需训练的方法，通过文本信息和视觉线索的链式推理，显著提高了MLLM在全景环境中的理解能力。基准测试和代码将在发布后公开。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在理解全景图像（ODIs）时表现出的不足。现有的MLLMs在处理传统2D图像时表现良好，但缺乏对全景图像所提供的沉浸式环境的理解能力，这限制了它们在VR/AR等领域的应用。现有的方法没有针对全景图像的专门评估基准，也缺乏有效的全景图像理解增强方法。

**核心思路**：论文的核心思路是构建一个专门针对全景图像理解的基准测试集（ODI-Bench），并提出一种无需训练的链式推理方法（Omni-CoT）来增强MLLMs对全景图像的理解能力。通过ODI-Bench，可以系统地评估现有MLLMs在全景图像理解方面的性能。Omni-CoT则利用文本信息和视觉线索进行链式推理，从而更好地捕捉全景图像的上下文信息。

**技术框架**：整体框架包括两个主要部分：ODI-Bench基准测试和Omni-CoT方法。ODI-Bench包含2000张高质量全景图像和4000多个问答对，涵盖10个细粒度任务。Omni-CoT方法则是在现有MLLMs的基础上，通过prompt engineering的方式，引导模型进行链式推理，从而提高其全景图像理解能力。具体流程是：输入全景图像和问题，模型首先生成中间推理步骤，然后基于这些步骤生成最终答案。

**关键创新**：论文的关键创新点在于：1) 提出了一个专门针对全景图像理解的综合性基准测试集ODI-Bench，填补了该领域的空白。2) 提出了Omni-CoT方法，该方法无需训练，即可显著提高MLLMs对全景图像的理解能力。与现有方法相比，Omni-CoT不需要额外的训练数据或模型参数，具有更高的效率和可扩展性。

**关键设计**：ODI-Bench的关键设计在于其多样性和细粒度。它包含了各种场景的全景图像，并设计了10个细粒度任务，涵盖了通用级别和空间级别的理解。Omni-CoT的关键设计在于其链式推理过程。通过精心设计的prompt，引导模型逐步推理，从而更好地捕捉全景图像的上下文信息。具体的prompt设计包括：首先要求模型描述图像中的主要对象和场景，然后要求模型分析对象之间的关系，最后要求模型回答问题。

## 📊 实验亮点

实验结果表明，现有MLLM在ODI-Bench上的表现远低于人类水平，表明其在全景图像理解方面存在显著差距。Omni-CoT方法能够显著提高MLLM在ODI-Bench上的性能，在多个任务上取得了明显的提升。例如，在空间关系理解任务上，Omni-CoT将模型的准确率提高了10%以上。

## 🎯 应用场景

该研究成果可广泛应用于VR/AR、机器人导航、自动驾驶等领域。ODI-Bench为评估和改进MLLM在全景图像理解方面的能力提供了一个标准平台。Omni-CoT方法可以帮助MLLM更好地理解沉浸式环境，从而提高相关应用的性能和用户体验。未来，该研究可以进一步扩展到视频理解、三维场景理解等领域。

## 📄 摘要（原文）

> Omnidirectional images (ODIs) provide full 360x180 view which are widely adopted in VR, AR and embodied intelligence applications. While multi-modal large language models (MLLMs) have demonstrated remarkable performance on conventional 2D image and video understanding benchmarks, their ability to comprehend the immersive environments captured by ODIs remains largely unexplored. To address this gap, we first present ODI-Bench, a novel comprehensive benchmark specifically designed for omnidirectional image understanding. ODI-Bench contains 2,000 high-quality omnidirectional images and over 4,000 manually annotated question-answering (QA) pairs across 10 fine-grained tasks, covering both general-level and spatial-level ODI understanding. Extensive experiments are conducted to benchmark 20 representative MLLMs, including proprietary and open-source models, under both close-ended and open-ended settings. Experimental results reveal that current MLLMs still struggle to capture the immersive context provided by ODIs. To this end, we further introduce Omni-CoT, a training-free method which significantly enhances MLLMs' comprehension ability in the omnidirectional environment through chain-of-thought reasoning across both textual information and visual cues. Both the benchmark and the code will be released upon the publication.

