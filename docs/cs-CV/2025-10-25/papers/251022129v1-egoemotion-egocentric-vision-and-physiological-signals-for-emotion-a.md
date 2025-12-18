---
layout: default
title: egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-World Tasks
---

# egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-World Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22129" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22129v1</a>
  <a href="https://arxiv.org/pdf/2510.22129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22129v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22129v1', 'egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-World Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthias Jammot, Björn Braun, Paul Streli, Rafael Wampfler, Christian Holz

**分类**: cs.CV, cs.HC

**发布日期**: 2025-10-25

**备注**: Accepted for publication at NeurIPS 2025

---

## 💡 一句话要点

**egoEMOTION：结合第一人称视觉与生理信号的情感与人格识别数据集**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `第一人称视觉` `情感识别` `人格识别` `生理信号` `数据集` `行为建模` `人机交互`

## 📋 核心要点

1. 现有第一人称视觉研究忽略了情感对行为的影响，限制了对人类行为的理解。
2. egoEMOTION数据集结合了第一人称视觉、生理信号和情感/人格自我报告，为情感驱动的行为建模提供数据基础。
3. 实验表明，基于第一人称视觉信号的情感预测优于基于生理信号的预测，验证了数据集的有效性。

## 📝 摘要（中文）

理解情感是预测人类行为的关键，但目前的第一人称视觉基准测试在很大程度上忽略了影响决策和行动的情绪状态。现有的第一人称感知任务侧重于物理活动、手-物交互和注意力建模，假设情感中性和人格统一。这限制了视觉系统捕捉行为关键内部驱动因素的能力。本文提出了egoEMOTION，这是第一个将第一人称视觉和生理信号与受控和真实场景中密集的情感和人格自我报告相结合的数据集。该数据集包含来自43名参与者的超过50小时的记录，使用Meta的Project Aria眼镜捕获。每个会话提供同步的眼动追踪视频、头戴式光电容积脉搏波描记法、惯性运动数据和生理基线作为参考。参与者完成了情绪诱发任务和自然活动，同时使用环状模型和Mikels' Wheel自我报告他们的情感状态，并通过大五模型报告他们的人格。我们定义了三个基准任务：（1）连续情感分类（效价、唤醒、支配）；（2）离散情感分类；（3）特质水平人格推断。我们表明，一种经典的基于学习的方法，作为真实世界情感预测中的一个简单基线，从第一人称视觉系统捕获的信号中产生的估计比处理生理信号更好。我们的数据集将情感和人格确立为第一人称感知中的核心维度，并开辟了情感驱动的行为、意图和交互建模的新方向。

## 🔬 方法详解

**问题定义**：现有第一人称视觉研究主要关注物理活动和物体交互，忽略了情感和人格等内在因素对行为的影响。这导致模型无法准确理解和预测人类行为，尤其是在复杂和动态的真实世界场景中。现有方法缺乏足够的数据和基准来评估情感和人格在第一人称感知中的作用。

**核心思路**：论文的核心思路是将情感和人格信息融入第一人称视觉感知中，认为这些内在因素是理解和预测人类行为的关键驱动力。通过构建一个包含丰富的视觉、生理和自我报告数据的数据集，旨在促进情感驱动的行为建模研究。

**技术框架**：egoEMOTION数据集的构建流程包括：1)招募参与者；2)使用Meta Project Aria眼镜收集第一人称视觉数据、生理信号（PPG、IMU）和眼动追踪数据；3)让参与者完成情绪诱发任务和自然活动；4)要求参与者使用环状模型、Mikels' Wheel和大五模型进行情感和人格的自我报告；5)同步所有数据并进行标注。基于该数据集，论文定义了三个基准任务：连续情感分类、离散情感分类和特质水平人格推断。

**关键创新**：egoEMOTION数据集的主要创新在于它是第一个将第一人称视觉、生理信号和情感/人格自我报告相结合的大规模数据集。它填补了第一人称视觉研究中情感和人格数据缺失的空白，为情感驱动的行为建模提供了新的研究方向。

**关键设计**：数据集使用了Meta Project Aria眼镜进行数据采集，保证了第一人称视觉数据的质量。生理信号的采集使用了头戴式PPG传感器，方便且不影响参与者的自然活动。情感和人格的自我报告使用了标准化的心理学模型，保证了数据的可靠性和可比性。论文还提供了一套基准测试，包括连续情感分类（效价、唤醒、支配）、离散情感分类和特质水平人格推断，方便研究者进行模型评估和比较。

## 📊 实验亮点

论文通过实验验证了基于第一人称视觉信号的情感预测优于基于生理信号的预测。使用经典学习方法作为基线，在真实世界情感预测任务中，第一人称视觉信号表现出更好的估计效果。这表明第一人称视觉数据在情感识别方面具有重要价值，并为未来的研究提供了有益的参考。

## 🎯 应用场景

该研究成果可应用于情感计算、人机交互、虚拟现实、辅助驾驶等领域。例如，通过识别驾驶员的情绪状态，辅助驾驶系统可以提供更个性化的安全提醒和驾驶辅助。在人机交互中，理解用户的情感可以使机器人或虚拟助手提供更自然和有效的服务。未来，该数据集可以促进开发更智能、更人性化的AI系统。

## 📄 摘要（原文）

> Understanding affect is central to anticipating human behavior, yet current egocentric vision benchmarks largely ignore the person's emotional states that shape their decisions and actions. Existing tasks in egocentric perception focus on physical activities, hand-object interactions, and attention modeling - assuming neutral affect and uniform personality. This limits the ability of vision systems to capture key internal drivers of behavior. In this paper, we present egoEMOTION, the first dataset that couples egocentric visual and physiological signals with dense self-reports of emotion and personality across controlled and real-world scenarios. Our dataset includes over 50 hours of recordings from 43 participants, captured using Meta's Project Aria glasses. Each session provides synchronized eye-tracking video, headmounted photoplethysmography, inertial motion data, and physiological baselines for reference. Participants completed emotion-elicitation tasks and naturalistic activities while self-reporting their affective state using the Circumplex Model and Mikels' Wheel as well as their personality via the Big Five model. We define three benchmark tasks: (1) continuous affect classification (valence, arousal, dominance); (2) discrete emotion classification; and (3) trait-level personality inference. We show that a classical learning-based method, as a simple baseline in real-world affect prediction, produces better estimates from signals captured on egocentric vision systems than processing physiological signals. Our dataset establishes emotion and personality as core dimensions in egocentric perception and opens new directions in affect-driven modeling of behavior, intent, and interaction.

