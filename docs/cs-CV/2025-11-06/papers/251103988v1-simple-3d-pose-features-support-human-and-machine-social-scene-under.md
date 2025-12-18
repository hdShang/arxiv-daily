---
layout: default
title: Simple 3D Pose Features Support Human and Machine Social Scene Understanding
---

# Simple 3D Pose Features Support Human and Machine Social Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03988" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03988v1</a>
  <a href="https://arxiv.org/pdf/2511.03988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03988v1', 'Simple 3D Pose Features Support Human and Machine Social Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenshuo Qin, Leyla Isik

**分类**: cs.CV, q-bio.NC

**发布日期**: 2025-11-06

**备注**: 28 pages, 6 figures

---

## 💡 一句话要点

**提出基于3D姿态特征的人机社交场景理解方法，超越现有AI模型。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `3D姿态估计` `社交场景理解` `人机交互` `深度学习` `视觉特征` `行为识别` `人工智能`

## 📋 核心要点

1. 现有AI视觉模型在社交互动识别方面存在不足，无法有效利用3D姿态信息。
2. 论文提出利用3D人体姿态信息，特别是面部朝向等简单特征，来提升社交场景理解能力。
3. 实验表明，基于3D姿态特征的方法超越了现有AI模型，并能有效提升其性能。

## 📝 摘要（中文）

人类能够迅速且毫不费力地从视觉输入中提取关于他人社交互动的各种信息，从诸如两个人是否面对面之类的视觉空间线索到更高级别的信息。然而，支持这些能力的计算仍然知之甚少，并且社交互动识别仍然挑战着即使是最先进的AI视觉系统。本文假设人类依赖于3D视觉空间姿态信息来进行社交互动判断，而这在大多数AI视觉模型中是缺失的。为了验证这一点，我们结合了最先进的姿态和深度估计算法来提取描绘日常人类动作的短视频片段中人物的3D关节位置，并将它们预测人类社交互动判断的能力与当前的AI视觉模型进行了比较。惊人的是，3D关节位置优于大多数当前的AI视觉模型，揭示了关键的社交信息存在于显式的身体位置中，而不是大多数视觉模型的学习特征中，甚至包括用于提取关节位置的姿态模型的逐层嵌入。为了揭示人类用于进行社交判断的关键姿态特征，我们推导出一个紧凑的3D社交姿态特征集，仅描述视频中面部的3D位置和方向。我们发现这些最小的描述符与完整3D关节集的预测强度相匹配，并且在与它们的嵌入相结合时，显着提高了现成的AI视觉模型的性能。此外，每个现成的AI视觉模型中3D社交姿态特征的表示程度预测了该模型匹配人类社交判断的能力。总之，我们的发现提供了强有力的证据，表明人类的社交场景理解依赖于3D姿态的显式表示，并且可以由简单的、结构化的视觉空间原语来支持。

## 🔬 方法详解

**问题定义**：现有AI视觉模型在理解社交场景，特别是识别人类之间的互动关系时，表现不佳。它们通常依赖于学习到的特征，而忽略了显式的3D姿态信息，尤其是人体关节的3D位置和面部朝向等关键线索。这导致模型难以准确判断人物之间的社交关系和意图。

**核心思路**：论文的核心思路是强调3D姿态信息在社交场景理解中的重要性。作者认为，人类在进行社交判断时，会依赖于显式的3D姿态信息，例如人物之间的相对位置、面部朝向等。因此，通过提取和利用这些3D姿态特征，可以有效提升AI模型在社交场景理解方面的能力。

**技术框架**：该方法主要包含以下几个阶段：1) 使用姿态和深度估计算法从视频中提取人物的3D关节位置；2) 从3D关节位置中提取紧凑的3D社交姿态特征，例如面部位置和方向；3) 将提取的3D社交姿态特征与现有AI视觉模型的嵌入相结合；4) 使用结合后的特征进行社交互动判断，并与人类的判断进行比较。

**关键创新**：该论文的关键创新在于：1) 证明了显式的3D姿态信息在社交场景理解中的重要性，超越了现有AI模型学习到的特征；2) 提出了一个紧凑的3D社交姿态特征集，仅包含面部位置和方向等简单信息，但却能有效提升模型性能；3) 揭示了AI视觉模型中3D社交姿态特征的表示程度与模型匹配人类社交判断能力之间的关系。

**关键设计**：论文的关键设计包括：1) 使用现成的姿态和深度估计算法，避免了从头训练模型的复杂性；2) 设计了一个紧凑的3D社交姿态特征集，减少了计算量，并突出了关键信息；3) 将3D社交姿态特征与现有AI视觉模型的嵌入相结合，充分利用了现有模型的学习能力。

## 📊 实验亮点

实验结果表明，仅使用3D关节位置就能超越大多数现有AI视觉模型在社交互动判断方面的性能。更重要的是，仅包含面部位置和方向的紧凑3D社交姿态特征集，与完整3D关节集的预测强度相匹配，并且在与现有AI视觉模型的嵌入相结合时，显著提高了其性能。此外，模型中3D社交姿态特征的表示程度与模型匹配人类社交判断能力之间存在正相关关系。

## 🎯 应用场景

该研究成果可应用于社交机器人、智能监控、人机交互等领域。例如，社交机器人可以利用3D姿态信息更准确地理解人类的社交行为，从而做出更自然的反应。智能监控系统可以利用该技术识别异常社交行为，例如潜在的冲突或暴力事件。人机交互系统可以利用该技术更好地理解用户的意图，提供更个性化的服务。

## 📄 摘要（原文）

> Humans can quickly and effortlessly extract a variety of information about others' social interactions from visual input, ranging from visuospatial cues like whether two people are facing each other to higher-level information. Yet, the computations supporting these abilities remain poorly understood, and social interaction recognition continues to challenge even the most advanced AI vision systems. Here, we hypothesized that humans rely on 3D visuospatial pose information to make social interaction judgments, which is absent in most AI vision models. To test this, we combined state-of-the-art pose and depth estimation algorithms to extract 3D joint positions of people in short video clips depicting everyday human actions and compared their ability to predict human social interaction judgments with current AI vision models. Strikingly, 3D joint positions outperformed most current AI vision models, revealing that key social information is available in explicit body position but not in the learned features of most vision models, including even the layer-wise embeddings of the pose models used to extract joint positions. To uncover the critical pose features humans use to make social judgments, we derived a compact set of 3D social pose features describing only the 3D position and direction of faces in the videos. We found that these minimal descriptors matched the predictive strength of the full set of 3D joints and significantly improved the performance of off-the-shelf AI vision models when combined with their embeddings. Moreover, the degree to which 3D social pose features were represented in each off-the-shelf AI vision model predicted the model's ability to match human social judgments. Together, our findings provide strong evidence that human social scene understanding relies on explicit representations of 3D pose and can be supported by simple, structured visuospatial primitives.

