---
layout: default
title: "FEAST: A Flexible Mealtime-Assistance System Towards In-the-Wild Personalization"
---

# FEAST: A Flexible Mealtime-Assistance System Towards In-the-Wild Personalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14968" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14968v2</a>
  <a href="https://arxiv.org/pdf/2506.14968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14968v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14968v2', 'FEAST: A Flexible Mealtime-Assistance System Towards In-the-Wild Personalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rajat Kumar Jenamani, Tom Silver, Ben Dodson, Shiqin Tong, Anthony Song, Yuting Yang, Ziang Liu, Benjamin Howe, Aimee Whitneck, Tapomayukh Bhattacharjee

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-17 (更新: 2025-06-27)

**备注**: RSS 2025 - Best Paper Award

---

## 💡 一句话要点

**提出FEAST系统以解决个性化餐饮辅助问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `餐饮辅助` `个性化服务` `模块化设计` `行为树` `家庭护理` `机器人技术`

## 📋 核心要点

1. 现有的餐饮辅助机器人在家庭环境中面临多样化活动和用户偏好的挑战，难以实现有效的个性化服务。
2. FEAST系统通过模块化硬件和多种交互方式，结合大语言模型的参数化行为树，实现灵活的个性化调整。
3. 实验结果显示，FEAST在满足用户个性化需求方面表现优于传统固定定制系统，用户能够成功调整系统以适应自身需求。

## 📝 摘要（中文）

物理护理机器人有望改善全球数百万需要喂养帮助的人的生活质量。然而，由于在家庭环境中餐饮辅助面临多样化活动、上下文、食物种类和用户偏好的挑战，现有方法难以满足个性化需求。本文提出FEAST，一个灵活的餐饮辅助系统，能够在实际环境中进行个性化调整，以满足个体护理对象的独特需求。该系统基于适应性、透明性和安全性三大原则，通过模块化硬件、丰富的交互方式和可参数化的行为树实现个性化。实验结果表明，FEAST在透明性和安全性方面表现优异，超越了固定定制的先进基线。通过与社区研究者的合作，进行的家庭用户研究验证了其实际应用性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有餐饮辅助机器人在家庭环境中无法满足多样化用户需求的问题。现有方法通常依赖于固定的定制选项，缺乏灵活性和适应性。

**核心思路**：FEAST系统的核心思路是通过模块化设计和多种交互方式，结合大语言模型的能力，实现个性化的餐饮辅助服务。这样的设计使得系统能够根据用户的具体需求进行动态调整。

**技术框架**：FEAST的整体架构包括模块化硬件（支持喂养、饮水和擦嘴的切换）、多样的交互方式（如网页界面、头部手势和物理按钮）以及可参数化的行为树。系统通过这些模块协同工作，提供个性化服务。

**关键创新**：FEAST的主要创新在于其灵活的模块化设计和基于大语言模型的行为树，允许用户在实际使用中进行透明和安全的个性化调整。这与现有方法的固定定制选项形成了鲜明对比。

**关键设计**：系统的关键设计包括模块化硬件的构建、支持多种交互方式的用户界面设计，以及行为树的参数化设置，确保系统能够在不同场景下安全有效地运行。

## 📊 实验亮点

在实验中，FEAST系统成功满足了用户的个性化需求，用户能够根据自身偏好调整系统设置。与固定定制的先进基线相比，FEAST在透明性和安全性方面表现出色，提供了更广泛的适应性。

## 🎯 应用场景

FEAST系统的潜在应用领域包括家庭护理、老年人照护和残疾人辅助等。其灵活的个性化能力能够显著提高用户的生活质量，未来可能在智能家居和机器人护理领域发挥重要作用。

## 📄 摘要（原文）

> Physical caregiving robots hold promise for improving the quality of life of millions worldwide who require assistance with feeding. However, in-home meal assistance remains challenging due to the diversity of activities (e.g., eating, drinking, mouth wiping), contexts (e.g., socializing, watching TV), food items, and user preferences that arise during deployment. In this work, we propose FEAST, a flexible mealtime-assistance system that can be personalized in-the-wild to meet the unique needs of individual care recipients. Developed in collaboration with two community researchers and informed by a formative study with a diverse group of care recipients, our system is guided by three key tenets for in-the-wild personalization: adaptability, transparency, and safety. FEAST embodies these principles through: (i) modular hardware that enables switching between assisted feeding, drinking, and mouth-wiping, (ii) diverse interaction methods, including a web interface, head gestures, and physical buttons, to accommodate diverse functional abilities and preferences, and (iii) parameterized behavior trees that can be safely and transparently adapted using a large language model. We evaluate our system based on the personalization requirements identified in our formative study, demonstrating that FEAST offers a wide range of transparent and safe adaptations and outperforms a state-of-the-art baseline limited to fixed customizations. To demonstrate real-world applicability, we conduct an in-home user study with two care recipients (who are community researchers), feeding them three meals each across three diverse scenarios. We further assess FEAST's ecological validity by evaluating with an Occupational Therapist previously unfamiliar with the system. In all cases, users successfully personalize FEAST to meet their individual needs and preferences. Website: https://emprise.cs.cornell.edu/feast

