---
layout: default
title: Look before Transcription: End-to-End SlideASR with Visually-Anchored Policy Optimization
---

# Look before Transcription: End-to-End SlideASR with Visually-Anchored Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08618" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08618v1</a>
  <a href="https://arxiv.org/pdf/2510.08618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08618v1" onclick="toggleFavorite(this, '2510.08618v1', 'Look before Transcription: End-to-End SlideASR with Visually-Anchored Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Hu, Delai Qiu, Yining Wang, Shengping Liu, Jitao Sang

**分类**: eess.AS, cs.CV, cs.SD

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出VAPO，通过视觉锚定的策略优化，提升SlideASR中领域术语的识别精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动语音识别` `多模态学习` `视觉锚定` `策略优化` `强化学习`

## 📋 核心要点

1. 现有ASR系统在处理学术讲座等专业场景中的领域术语时，准确率较低，传统方法复杂且效果不佳。
2. 论文提出视觉锚定的策略优化（VAPO），通过强化学习，使模型遵循“先看后转录”的流程，提升识别精度。
3. 实验结果表明，VAPO显著提高了领域特定术语的识别率，并在SlideASR-Bench数据集上取得了优异表现。

## 📝 摘要（中文）

自动语音识别（ASR）系统在特定领域的术语识别方面面临挑战，尤其是在学术讲座等专业场景中。为了解决这个问题，我们定义了SlideASR任务，该任务利用演示幻灯片中的丰富视觉信息来提高转录准确率。现有的流水线方法通常复杂且效果不佳。尽管全模态大型语言模型（OLLM）提供了一个有前景的端到端框架，但它们在实践中经常退化为简单的光学字符识别（OCR）系统。为了克服这个问题，我们提出了一种新颖的后训练方法——视觉锚定的策略优化（VAPO），旨在控制模型的推理过程。借鉴思维链推理范式，VAPO使用<think><answer>格式强制执行结构化的“先看后转录”过程。具体来说，模型首先在think步骤中对幻灯片内容执行OCR，然后在answer步骤中通过参考此识别的视觉信息来生成转录。通过强化学习优化此推理过程，并使用四个不同的奖励来针对格式合规性、OCR准确性、ASR质量和视觉锚定一致性。为了支持进一步的研究，我们构建了SlideASR-Bench，这是一个新的实体丰富的基准，包含用于训练和测试的合成数据集，以及用于评估的具有挑战性的真实世界数据集。大量的实验表明，VAPO显着提高了领域特定术语的识别率，为SlideASR建立了一个有效的端到端范例。

## 🔬 方法详解

**问题定义**：论文旨在解决SlideASR任务中，现有方法（包括流水线方法和直接使用OLLM）无法有效利用幻灯片视觉信息，导致领域术语识别精度低的问题。现有流水线方法复杂，而OLLM容易退化为简单的OCR系统，忽略了语音信息。

**核心思路**：论文的核心思路是利用强化学习，引导模型模仿人类“先看幻灯片，再进行转录”的认知过程。通过引入<think><answer>的结构化推理格式，强制模型先进行OCR，再结合OCR结果进行语音转录，从而实现视觉信息和语音信息的有效融合。

**技术框架**：整体框架是一个端到端的模型，采用后训练的方式进行优化。主要流程包括：1) 输入幻灯片图像和语音；2) 模型生成<think>步骤，对幻灯片内容进行OCR；3) 模型生成<answer>步骤，结合OCR结果和语音信息进行转录；4) 使用强化学习，根据四个奖励函数优化模型的推理过程。

**关键创新**：最重要的创新点在于VAPO策略优化方法，它通过强化学习，显式地引导模型进行视觉锚定的推理。与直接训练OLLM相比，VAPO能够更好地控制模型的推理过程，避免模型退化为简单的OCR系统。

**关键设计**：VAPO的关键设计包括：1) <think><answer>的结构化推理格式，强制模型进行视觉推理；2) 四个奖励函数：格式合规性奖励、OCR准确性奖励、ASR质量奖励和视觉锚定一致性奖励。这些奖励函数共同引导模型学习有效的视觉锚定策略。具体参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，VAPO在SlideASR任务中取得了显著的性能提升。在SlideASR-Bench数据集上，VAPO能够有效提高领域特定术语的识别精度，优于现有的流水线方法和直接使用OLLM的方法。具体的性能数据和提升幅度在论文中进行了详细的展示，属于未知信息。

## 🎯 应用场景

该研究成果可应用于在线教育、会议记录、学术讲座等场景，提高语音转录的准确性和效率。通过利用视觉信息，可以更好地识别领域术语和专业知识，为用户提供更准确、更可靠的语音转录服务。未来，该方法可以推广到其他多模态语音识别任务中，例如视频字幕生成等。

## 📄 摘要（原文）

> Automatic speech recognition (ASR) systems often struggle with domain-specific terminology, especially in specialized settings such as academic lectures. To address this, we define the SlideASR task, which leverages the rich visual information from presentation slides to improve transcription accuracy. Existing pipeline methods for this task tend to be complex and underperform. Although omni-modal large language models (OLLMs) provide a promising end-to-end framework, they frequently fail in practice by degenerating into simple optical character recognition (OCR) systems. To overcome this, we propose Visually-Anchored Policy Optimization (VAPO), a novel post-training method designed to control the model's reasoning process. Drawing on the Chain-of-Thought reasoning paradigm, VAPO enforces a structured "Look before Transcription" procedure using a <think><answer> format. Specifically, the model first performs OCR on the slide content within the think step, then generates the transcription by referencing this recognized visual information in the answer step. This reasoning process is optimized via reinforcement learning with four distinct rewards targeting format compliance, OCR accuracy, ASR quality, and visual anchoring consistency. To support further research, we construct SlideASR-Bench, a new entity-rich benchmark consisting of a synthetic dataset for training and testing, and a challenging real-world set for evaluation. Extensive experiments demonstrate that VAPO significantly improves recognition of domain-specific terms, establishing an effective end-to-end paradigm for SlideASR.

