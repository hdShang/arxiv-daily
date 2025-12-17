---
layout: default
title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
---

# Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14396" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14396v3</a>
  <a href="https://arxiv.org/pdf/2511.14396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14396v3" onclick="toggleFavorite(this, '2511.14396v3', 'Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiuxiu Qi, Yu Yang, Jiannong Cao, Luyao Bai, Chongshan Fan, Chengtai Cao, Hongpeng Wang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-11-18 (更新: 2025-12-12)

**备注**: Accepted at AAAI 2026, the Project website is available at https://qhemu.github.io/CCoL/

---

## 💡 一句话要点

**提出CCoL框架，通过语义-物理对齐的连续视觉-语言-动作协同学习提升行为克隆性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `行为克隆` `视觉语言动作` `协同学习` `语义物理对齐` `机器人操作` `人机交互`

## 📋 核心要点

1. 行为克隆面临序列动作决策中的累积误差问题，现有方法在物理不连续性和语义-物理不对齐方面存在不足。
2. CCoL框架通过连续协同学习视觉、语言和本体感受信息，并利用双向交叉注意力实现语义-物理对齐，从而生成更鲁棒的动作轨迹。
3. 实验结果表明，CCoL在模拟和真实机器人任务中均取得了显著的性能提升，尤其在双手动插入等复杂任务中表现突出。

## 📝 摘要（中文）

本文提出了一种名为连续视觉-语言-动作协同学习与语义-物理对齐（CCoL）的新型行为克隆（BC）框架，旨在确保时间上一致的执行和细粒度的语义对齐。该框架通过视觉、语言和本体感受输入（例如，机器人内部状态）的连续协同学习，生成鲁棒且平滑的动作执行轨迹。同时，通过双向交叉注意力将语言语义锚定到视觉运动表示，学习用于动作生成的上下文信息，成功克服了语义-物理不对齐的问题。大量实验表明，CCoL在三个模拟套件中实现了平均8.0%的相对改进，在人工演示的双手动插入任务中获得了高达19.2%的相对增益。在7自由度机器人上的真实世界测试进一步证实了CCoL在未见和嘈杂物体状态下的泛化能力。

## 🔬 方法详解

**问题定义**：行为克隆（BC）旨在模仿人类演示学习控制策略，但由于序列动作决策中的累积误差，导致性能下降。现有方法难以解决物理不连续性和语义-物理不对齐问题，使得动作克隆不准确，执行断断续续。

**核心思路**：CCoL的核心在于通过连续协同学习视觉、语言和本体感受信息，生成平滑的动作轨迹，并利用语义-物理对齐来克服语义鸿沟。通过这种方式，模型能够更好地理解语言指令，并将其转化为精确的机器人动作。

**技术框架**：CCoL框架包含视觉编码器、语言编码器和动作生成器。视觉编码器处理图像输入，语言编码器处理语言指令，动作生成器则根据视觉和语言信息生成动作序列。关键在于，视觉、语言和本体感受信息在整个过程中进行连续协同学习，以确保时间一致性。此外，还使用了双向交叉注意力机制来实现语义-物理对齐。

**关键创新**：CCoL的关键创新在于其连续协同学习和语义-物理对齐机制。传统的BC方法通常独立处理视觉和语言信息，而CCoL则将它们整合到一个统一的学习框架中。通过双向交叉注意力，模型能够学习到语言语义与视觉运动表示之间的对应关系，从而更好地理解语言指令并生成相应的动作。

**关键设计**：CCoL使用了Transformer架构来实现双向交叉注意力。损失函数包括行为克隆损失、平滑损失和对齐损失。行为克隆损失用于模仿人类演示，平滑损失用于生成平滑的动作轨迹，对齐损失用于促进语义-物理对齐。具体参数设置（如Transformer层数、注意力头数等）根据实验结果进行调整。

## 📊 实验亮点

CCoL在三个模拟套件中实现了平均8.0%的相对改进，在人工演示的双手动插入任务中获得了高达19.2%的相对增益。与现有方法相比，CCoL能够生成更鲁棒、更平滑的动作轨迹，并更好地泛化到未见过的物体状态。真实机器人实验也验证了CCoL的有效性。

## 🎯 应用场景

CCoL框架可应用于各种需要人机协作的机器人操作任务，例如装配、抓取、放置等。该技术能够提升机器人在复杂环境下的操作能力，并降低对人工示教数据的依赖。未来，CCoL有望应用于智能制造、医疗机器人、家庭服务机器人等领域，实现更智能、更高效的人机交互。

## 📄 摘要（原文）

> Language-conditioned manipulation facilitates human-robot interaction via behavioral cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (e.g., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL's generalization under unseen and noisy object states.

