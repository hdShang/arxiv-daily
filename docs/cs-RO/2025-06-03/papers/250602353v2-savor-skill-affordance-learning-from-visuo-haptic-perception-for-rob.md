---
layout: default
title: "SAVOR: Skill Affordance Learning from Visuo-Haptic Perception for Robot-Assisted Bite Acquisition"
---

# SAVOR: Skill Affordance Learning from Visuo-Haptic Perception for Robot-Assisted Bite Acquisition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02353" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02353v2</a>
  <a href="https://arxiv.org/pdf/2506.02353.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02353v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02353v2', 'SAVOR: Skill Affordance Learning from Visuo-Haptic Perception for Robot-Assisted Bite Acquisition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhanxin Wu, Bo Ai, Tom Silver, Tapomayukh Bhattacharjee

**分类**: cs.RO

**发布日期**: 2025-06-03 (更新: 2025-09-01)

**备注**: Conference on Robot Learning, Oral

---

## 💡 一句话要点

**提出SAVOR以解决机器人辅助进食中的咬取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人辅助进食` `技能可用性` `多模态感知` `工具与食物交互` `动态调整` `进食成功率提升`

## 📋 核心要点

1. 现有的机器人辅助进食方法在处理复杂的餐具与食物交互时存在可靠性不足的问题，尤其是食物属性的变化使得咬取变得更加困难。
2. SAVOR方法通过结合工具可用性和食物可用性，利用离线学习和在线多模态感知，动态调整操作技能的适用性，从而提高咬取成功率。
3. 在20种单一食物和10种实际餐食的评估中，SAVOR方法相较于现有的基于类别的方法，成功率提升了13%，显示出其有效性和通用性。

## 📝 摘要（中文）

机器人辅助进食需要可靠的咬取能力，但由于餐具与食物之间复杂的物理交互，这一任务面临挑战。食物属性的时间变化（如牛排在冷却过程中变硬）进一步增加了难度。为此，本文提出SAVOR，一种新颖的技能可用性学习方法，旨在评估特定餐具与食物交互下的操作技能适用性。该方法通过离线校准学习餐具的功能能力，并利用视觉-触觉感知动态调整食物属性，实时预测技能可用性，从而提高咬取成功率。实验结果显示，该方法在20种单一食物和10种实际餐食中，相较于最先进的方法提升了13%的咬取成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人辅助进食中的咬取能力不足问题，现有方法在处理餐具与食物的复杂交互时，往往无法适应食物属性的动态变化，导致咬取失败。

**核心思路**：SAVOR通过学习技能可用性，结合工具和食物的可用性，实时评估不同操作技能的适用性，以应对多变的食物属性。该方法设计旨在提升机器人在实际进食场景中的表现。

**技术框架**：SAVOR的整体架构包括离线学习和在线感知两个阶段。离线阶段通过校准不同餐具与多种食物的交互，建立工具可用性模型；在线阶段则利用视觉-触觉感知动态更新食物属性，实时预测技能可用性。

**关键创新**：SAVOR的核心创新在于将工具可用性与食物可用性相结合，形成动态的技能可用性评估机制。这一方法与传统的基于类别的技能选择方法有本质区别，能够更好地适应复杂的进食场景。

**关键设计**：在技术细节上，SAVOR采用了视觉条件语言模型进行食物属性的初步推断，并通过多模态感知进行动态调整。损失函数设计考虑了技能选择的准确性与实时性，以确保机器人在实际操作中的高效性。

## 📊 实验亮点

在实验中，SAVOR方法在20种单一食物和10种实际餐食的评估中，咬取成功率提升了13%，相较于最先进的基于类别的方法表现更为优越。这一结果表明，动态建模技能可用性对于实现有效的机器人辅助进食至关重要。

## 🎯 应用场景

该研究的潜在应用场景包括老年人和残疾人辅助进食、餐厅自动化服务以及家庭机器人等领域。通过提高机器人在复杂进食环境中的适应能力，SAVOR有望显著提升人机交互的质量和效率，推动智能机器人在日常生活中的普及与应用。

## 📄 摘要（原文）

> Robot-assisted feeding requires reliable bite acquisition, a challenging task due to the complex interactions between utensils and food with diverse physical properties. These interactions are further complicated by the temporal variability of food properties-for example, steak becomes firm as it cools even during a meal. To address this, we propose SAVOR, a novel approach for learning skill affordances for bite acquisition-how suitable a manipulation skill (e.g., skewering, scooping) is for a given utensil-food interaction. In our formulation, skill affordances arise from the combination of tool affordances (what a utensil can do) and food affordances (what the food allows). Tool affordances are learned offline through calibration, where different utensils interact with a variety of foods to model their functional capabilities. Food affordances are characterized by physical properties such as softness, moisture, and viscosity, initially inferred through commonsense reasoning using a visually-conditioned language model and then dynamically refined through online multi-modal visuo-haptic perception using SAVOR-Net during interaction. Our method integrates these offline and online estimates to predict skill affordances in real time, enabling the robot to select the most appropriate skill for each food item. Evaluated on 20 single-item foods and 10 in-the-wild meals, our approach improves bite acquisition success rate by 13% over state-of-the-art (SOTA) category-based methods (e.g. use skewer for fruits). These results highlight the importance of modeling interaction-driven skill affordances for generalizable and effective robot-assisted bite acquisition. Website: https://emprise.cs.cornell.edu/savor/

