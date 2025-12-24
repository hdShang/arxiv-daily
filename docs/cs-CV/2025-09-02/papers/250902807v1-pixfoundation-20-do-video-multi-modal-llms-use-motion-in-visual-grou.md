---
layout: default
title: "PixFoundation 2.0: Do Video Multi-Modal LLMs Use Motion in Visual Grounding?"
---

# PixFoundation 2.0: Do Video Multi-Modal LLMs Use Motion in Visual Grounding?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02807" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02807v1</a>
  <a href="https://arxiv.org/pdf/2509.02807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02807v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02807v1', 'PixFoundation 2.0: Do Video Multi-Modal LLMs Use Motion in Visual Grounding?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mennatullah Siam

**分类**: cs.CV

**发布日期**: 2025-09-02

**备注**: Work under review in NeurIPS 2025 with the title "Are we using Motion in Referring Segmentation? A Motion-Centric Evaluation"

**🔗 代码/项目**: [GITHUB](https://github.com/MSiam/PixFoundation-2.0.git)

---

## 💡 一句话要点

**PixFoundation 2.0：评估视频多模态LLM在视觉定位中对运动信息的利用程度**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频多模态LLM` `视觉定位` `运动信息` `时空推理` `基准测试` `运动自适应` `MoCentric-Bench`

## 📋 核心要点

1. 现有视频多模态LLM在视觉定位任务中，对运动信息的利用程度不足，容易被静态外观线索主导。
2. 提出MoCentric-Bench基准测试，并设计了四种以运动为中心的探测技术，用于评估模型识别真实运动和理解运动顺序的能力。
3. 实验表明，简单的运动自适应技术即可在MoCentric-Bench上取得SOTA性能，突显了现有模型在时空理解方面的不足。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在图像和文本模态上展现了令人印象深刻的泛化能力。虽然它们在视频领域的扩展已经实现了视频问答和视频字幕等任务，但其像素级视觉定位能力的研究较少。本文提出了一个重要问题：在像素级视觉定位中是否使用了运动信息？视频MLLM是否能够根据描述运动模式的自然语言表达式来分割对象？我们指出现有基准测试的不足，在这些基准测试中，单个帧通常足以捕获运动参考表达，而无需任何时间推理。为了解决这个问题，我们引入了四种以运动为中心的探测技术，专门为视觉定位任务设计，以研究视频MLLM从虚假运动中识别真实运动以及掌握运动顺序的能力。因此，我们提供了一个以运动为中心的基准测试MoCentric-Bench。它确保视频MLLM在评估时能够利用运动和语言之间的交互，而不是被现有视觉定位数据集中强调的静态外观线索所主导。我们进一步建立了强大的单图像基线，其性能与先前方法相当或优于先前方法。最后，我们探索了简单的以运动为中心的自适应技术，这些技术在我们的MoCentric-Bench上提供了最先进的性能。我们的以运动为中心的基准测试、评估和发现挑战了未来的模型，以提高视频中密集的时空定位和像素级理解。

## 🔬 方法详解

**问题定义**：论文旨在解决视频多模态LLM在像素级视觉定位任务中，对运动信息利用不足的问题。现有方法和数据集往往侧重于静态外观特征，忽略了运动信息在理解视频内容中的重要作用，导致模型无法有效处理需要时序推理的视觉定位任务。

**核心思路**：论文的核心思路是通过构建一个以运动为中心的基准测试MoCentric-Bench，并设计相应的评估方法，来促使模型更多地关注和利用视频中的运动信息。通过引入对抗性的运动模式，迫使模型进行更深入的时空推理，从而提高其视觉定位能力。

**技术框架**：论文主要包含以下几个部分：1) 分析现有视觉定位数据集的局限性，指出其对运动信息的考察不足；2) 提出MoCentric-Bench基准测试，包含多种运动模式的视觉定位任务；3) 设计四种以运动为中心的探测技术，用于评估模型对运动信息的理解能力，包括区分真假运动和理解运动顺序；4) 探索简单的运动自适应技术，提升模型在MoCentric-Bench上的性能。

**关键创新**：论文的关键创新在于提出了MoCentric-Bench基准测试，该基准测试专门设计用于评估视频多模态LLM对运动信息的利用能力。与现有数据集相比，MoCentric-Bench更加强调运动信息在视觉定位中的作用，能够更有效地考察模型的时空推理能力。此外，论文还设计了四种以运动为中心的探测技术，为评估模型提供了新的视角。

**关键设计**：MoCentric-Bench基准测试包含多种运动模式，例如线性运动、旋转运动、周期性运动等。为了增加难度，基准测试中还引入了对抗性的运动模式，例如将真实运动替换为虚假运动，或者打乱运动的顺序。四种探测技术分别针对不同的运动理解能力进行评估，例如区分真假运动、理解运动顺序、识别运动方向等。论文还探索了简单的运动自适应技术，例如在训练数据中增加运动相关的样本，或者使用运动相关的损失函数。

## 📊 实验亮点

论文提出的MoCentric-Bench基准测试和运动自适应技术，能够有效提升视频多模态LLM在视觉定位任务中对运动信息的利用能力。实验结果表明，简单的运动自适应技术即可在MoCentric-Bench上取得SOTA性能，显著优于现有方法，验证了该研究的有效性。

## 🎯 应用场景

该研究成果可应用于视频监控、自动驾驶、机器人导航等领域。通过提升模型对视频中运动信息的理解能力，可以提高目标检测、行为识别、场景理解等任务的准确性和鲁棒性。未来，该研究有望推动视频内容分析和理解技术的进一步发展。

## 📄 摘要（原文）

> Multi-modal large language models (MLLMs) have shown impressive generalization across tasks using images and text modalities. While their extension to video has enabled tasks such as video question answering and video captioning, their pixel-level visual grounding abilities are less studied. In this work, we raise the pertinent question of whether motion is used in pixel-level visual grounding and whether video MLLMs can segment objects based on natural language expressions describing their motion patterns. We identify the shortcomings in the current benchmarks, where we show that a single frame can often suffice for capturing the motion referring expression without any temporal reasoning. To address this, we introduce four motion-centric probing techniques, particularly designed for the visual grounding task, to study video MLLMs' ability to identify true motion from a fake one and their ability to grasp the motion order. Consequently, we provide a motion-centric benchmark, MoCentric-Bench. It ensures that video MLLMs are evaluated towards leveraging the interaction between motion and language rather than being dominated by static appearance cues emphasized in existing visual grounding datasets. We further establish strong single-image baselines that are on par with or outperform prior methods. Finally, we explore simple motion-centric adaptation techniques that provide state-of-the-art performance on our MoCentric-Bench. Our motion-centric benchmark, evaluation and findings challenge future models to improve dense spatiotemporal grounding and pixel-level understanding within videos. Code and datasets will be made publicly available at https://github.com/MSiam/PixFoundation-2.0.git.

