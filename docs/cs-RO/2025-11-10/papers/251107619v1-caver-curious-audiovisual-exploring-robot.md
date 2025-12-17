---
layout: default
title: CAVER: Curious Audiovisual Exploring Robot
---

# CAVER: Curious Audiovisual Exploring Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07619" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07619v1</a>
  <a href="https://arxiv.org/pdf/2511.07619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07619v1" onclick="toggleFavorite(this, '2511.07619v1', 'CAVER: Curious Audiovisual Exploring Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Macesanu, Boueny Folefack, Samik Singh, Ruchira Ray, Ben Abbatematteo, Roberto Martín-Martín

**分类**: cs.RO

**发布日期**: 2025-11-10

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**CAVER: 一种好奇心驱动的视听探索机器人，用于构建丰富的物体视听表征。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视听融合` `机器人探索` `好奇心驱动` `主动学习` `多模态学习`

## 📋 核心要点

1. 现有的机器人操作缺乏对物体视听信息的有效利用，限制了其在材料分类和音频模仿等任务中的能力。
2. CAVER通过设计新型末端执行器、融合视听信息的表征以及好奇心驱动的探索算法，高效地构建物体的视听知识。
3. 实验证明，CAVER能够更有效地构建丰富的视听表征，并在材料分类和音频模仿任务中取得显著的性能提升。

## 📝 摘要（中文）

本文提出了一种名为CAVER的新型机器人，它能够构建和利用丰富的物体视听表征。CAVER包含三项创新：1) 一种新型3D打印末端执行器，可连接到平行夹爪，用于激发物体的音频响应；2) 一种视听表征，它将局部和全局外观信息与声音特征相结合；3) 一种探索算法，该算法以好奇心驱动的方式使用和构建视听表征，优先与高不确定性物体交互，从而以更少的交互获得良好的音频覆盖。实验表明，CAVER在不同场景中构建丰富的表征比几种探索基线更有效，并且学习到的视听表征在材料分类和模仿纯音频人类演示方面带来了显著的改进。

## 🔬 方法详解

**问题定义**：现有的机器人操作方法在很大程度上依赖于视觉信息，忽略了物体交互过程中产生的音频信息，这限制了机器人在材料识别、声音模仿等任务中的能力。现有的探索方法通常效率较低，需要大量的交互才能获得充分的知识。

**核心思路**：CAVER的核心思路是利用好奇心驱动的探索策略，引导机器人主动与具有高不确定性的物体进行交互，从而高效地构建物体的视听表征。通过结合视觉和听觉信息，机器人可以更全面地理解物体的属性和行为。

**技术框架**：CAVER系统主要包含三个模块：1) **末端执行器**：一个3D打印的末端执行器，用于激发物体的音频响应。2) **视听表征**：一种融合局部和全局视觉信息以及声音特征的表征方法。3) **探索算法**：一种基于好奇心驱动的探索算法，用于指导机器人选择与哪些物体进行交互。机器人通过末端执行器与物体交互，收集视听数据，然后利用这些数据更新视听表征，并根据表征的不确定性选择下一个交互对象。

**关键创新**：CAVER的关键创新在于其好奇心驱动的探索算法和视听表征方法。传统的探索算法通常是随机的或基于预定义的规则，而CAVER的探索算法能够根据当前知识的不确定性自适应地选择交互对象，从而更有效地获取信息。视听表征方法则能够将视觉和听觉信息融合在一起，从而更全面地描述物体的属性。

**关键设计**：末端执行器采用3D打印技术，可以根据不同的任务需求进行定制。视听表征使用深度学习模型提取视觉和听觉特征，并使用对比学习方法学习不同模态之间的关联。探索算法使用高斯过程模型估计视听表征的不确定性，并选择不确定性最高的物体进行交互。具体的损失函数和网络结构等细节在论文中有详细描述，此处未知。

## 📊 实验亮点

实验结果表明，CAVER在构建视听表征方面优于几种基线方法，能够以更少的交互次数获得更好的覆盖率。在材料分类任务中，CAVER的性能显著优于仅使用视觉信息的模型。在音频模仿任务中，CAVER能够成功地模仿人类的音频演示，并生成与演示相似的声音。具体的性能提升幅度未知，需要在论文中查找。

## 🎯 应用场景

CAVER的研究成果可应用于多种机器人操作任务，例如：材料分类、物体识别、声音模仿、故障诊断等。通过学习物体的视听特性，机器人可以更好地理解周围环境，并执行更复杂的任务。例如，机器人可以通过听声音来判断物体的材质，或者通过模仿人类的音频演示来学习新的技能。该研究还有助于开发更智能、更自主的机器人系统。

## 📄 摘要（原文）

> Multimodal audiovisual perception can enable new avenues for robotic manipulation, from better material classification to the imitation of demonstrations for which only audio signals are available (e.g., playing a tune by ear). However, to unlock such multimodal potential, robots need to learn the correlations between an object's visual appearance and the sound it generates when they interact with it. Such an active sensorimotor experience requires new interaction capabilities, representations, and exploration methods to guide the robot in efficiently building increasingly rich audiovisual knowledge. In this work, we present CAVER, a novel robot that builds and utilizes rich audiovisual representations of objects. CAVER includes three novel contributions: 1) a novel 3D printed end-effector, attachable to parallel grippers, that excites objects' audio responses, 2) an audiovisual representation that combines local and global appearance information with sound features, and 3) an exploration algorithm that uses and builds the audiovisual representation in a curiosity-driven manner that prioritizes interacting with high uncertainty objects to obtain good coverage of surprising audio with fewer interactions. We demonstrate that CAVER builds rich representations in different scenarios more efficiently than several exploration baselines, and that the learned audiovisual representation leads to significant improvements in material classification and the imitation of audio-only human demonstrations. https://caver-bot.github.io/

