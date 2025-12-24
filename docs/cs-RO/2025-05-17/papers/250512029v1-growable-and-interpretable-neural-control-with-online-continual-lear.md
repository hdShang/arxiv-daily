---
layout: default
title: Growable and Interpretable Neural Control with Online Continual Learning for Autonomous Lifelong Locomotion Learning Machines
---

# Growable and Interpretable Neural Control with Online Continual Learning for Autonomous Lifelong Locomotion Learning Machines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12029" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12029v1</a>
  <a href="https://arxiv.org/pdf/2505.12029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12029v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12029v1', 'Growable and Interpretable Neural Control with Online Continual Learning for Autonomous Lifelong Locomotion Learning Machines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arthicha Srisuchinnawong, Poramate Manoonpong

**分类**: cs.RO

**发布日期**: 2025-05-17

**备注**: Accepted Manuscript (IJRR). The International Journal of Robotics Research. 2025

**DOI**: [10.1177/02783649251336385](https://doi.org/10.1177/02783649251336385)

---

## 💡 一句话要点

**提出GOLLUM以解决持续运动学习中的四大挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `持续学习` `可解释性` `神经发生` `机器人技能` `自主学习` `运动学习` `六足机器人`

## 📋 核心要点

1. 现有的持续运动学习方法面临不可理解性、样本效率低、知识利用不足和灾难性遗忘等四大挑战。
2. 本文提出的GOLLUM框架通过可解释性特征，利用神经发生技术无监督地扩展技能编码，解决了上述问题。
3. 在实验中，GOLLUM在一小时内成功地在六足机器人上自主学习多种运动技能，并有效结合先前技能以促进新技能的学习。

## 📝 摘要（中文）

持续运动学习面临四个挑战：不可理解性、样本效率低、知识利用不足和灾难性遗忘。为此，本文提出了可扩展的在线运动学习框架GOLLUM，利用可解释性特征来应对上述挑战。GOLLUM具有两种可解释性维度：层级可解释性用于神经控制功能编码，列级可解释性用于机器人技能编码。通过这种可解释的控制结构，GOLLUM利用神经发生无监督地增加列（环状网络），每列分别训练以编码和维持特定的主要机器人技能。GOLLUM还通过添加新的神经映射层进行在线补充学习，将参数转移到新技能上，并补充已获得技能的组合。在物理六足机器人上，GOLLUM成功地在一小时内自主且持续地获得多种运动技能（如行走、爬坡和弹跳），并展示了结合先前学习技能以促进新技能学习的能力，同时防止灾难性遗忘。

## 🔬 方法详解

**问题定义**：本文旨在解决持续运动学习中的四个主要挑战：不可理解性、样本效率低、知识利用不足和灾难性遗忘。现有方法往往无法有效应对这些问题，导致学习过程不稳定和效率低下。

**核心思路**：GOLLUM框架通过引入可解释性特征，利用神经发生技术无监督地扩展技能编码。每个技能通过独立的列进行编码，从而提高了学习的灵活性和效率。

**技术框架**：GOLLUM的整体架构包括两个主要模块：一是层级可解释性模块，用于神经控制功能的编码；二是列级可解释性模块，用于机器人技能的编码。通过这两个模块，GOLLUM能够有效地管理和扩展技能。

**关键创新**：GOLLUM的最大创新在于其可解释性结构和神经发生技术的结合，使得机器人能够在没有人类干预的情况下自主学习和适应新环境。这一设计显著区别于现有的运动学习方法。

**关键设计**：GOLLUM采用环状网络结构，每个列独立训练以编码特定技能。此外，通过在线补充学习，GOLLUM能够将新技能的参数转移并结合已学技能，确保学习过程的连贯性和稳定性。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在实验中，GOLLUM成功地在一小时内自主学习了多种运动技能，包括行走、爬坡和弹跳，且能够有效结合先前学习的技能以促进新技能的学习。与现有方法相比，GOLLUM在解决灾难性遗忘和提高样本效率方面表现出显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能制造和人机协作等。GOLLUM框架的可解释性和自主学习能力使其在动态环境中表现出色，未来可广泛应用于需要持续学习和适应的场景，如救援机器人和探索机器人等。

## 📄 摘要（原文）

> Continual locomotion learning faces four challenges: incomprehensibility, sample inefficiency, lack of knowledge exploitation, and catastrophic forgetting. Thus, this work introduces Growable Online Locomotion Learning Under Multicondition (GOLLUM), which exploits the interpretability feature to address the aforementioned challenges. GOLLUM has two dimensions of interpretability: layer-wise interpretability for neural control function encoding and column-wise interpretability for robot skill encoding. With this interpretable control structure, GOLLUM utilizes neurogenesis to unsupervisely increment columns (ring-like networks); each column is trained separately to encode and maintain a specific primary robot skill. GOLLUM also transfers the parameters to new skills and supplements the learned combination of acquired skills through another neural mapping layer added (layer-wise) with online supplementary learning. On a physical hexapod robot, GOLLUM successfully acquired multiple locomotion skills (e.g., walking, slope climbing, and bouncing) autonomously and continuously within an hour using a simple reward function. Furthermore, it demonstrated the capability of combining previous learned skills to facilitate the learning process of new skills while preventing catastrophic forgetting. Compared to state-of-the-art locomotion learning approaches, GOLLUM is the only approach that addresses the four challenges above mentioned without human intervention. It also emphasizes the potential exploitation of interpretability to achieve autonomous lifelong learning machines.

