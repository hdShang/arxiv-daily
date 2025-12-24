---
layout: default
title: LLM-Based Authoring of Agent-Based Narratives through Scene Descriptions
---

# LLM-Based Authoring of Agent-Based Narratives through Scene Descriptions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20550" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20550v1</a>
  <a href="https://arxiv.org/pdf/2512.20550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20550v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20550v1', 'LLM-Based Authoring of Agent-Based Narratives through Scene Descriptions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vinayak Regmi, Christos Mousas

**分类**: cs.GR

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出一种基于LLM的叙事生成系统，通过场景描述驱动Agent行为。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent叙事生成` `大型语言模型` `程序化内容生成` `虚拟Agent` `场景描述`

## 📋 核心要点

1. 现有Agent叙事生成方法缺乏灵活性和可扩展性，难以快速原型设计复杂的交互场景。
2. 利用LLM的强大语言理解和生成能力，将场景描述转化为Agent的行为序列，实现叙事生成。
3. 实验表明，该系统能够有效地将场景描述转化为可执行的Agent行为，并评估了不同LLM的性能。

## 📝 摘要（中文）

本文提出了一种利用大型语言模型（LLM）程序化生成基于Agent的叙事的系统。用户可以将多个Agent和对象拖放到场景中，每个实体都会自动分配语义元数据，描述其身份、角色和潜在交互。然后，场景结构被序列化为自然语言提示，并发送给LLM，LLM返回一个结构化的字符串，描述Agent和对象之间的一系列动作和交互。返回的字符串编码了谁执行了哪些动作、何时以及如何执行。自定义解析器解释这个字符串，并触发协调的Agent行为、动画和交互模块。该系统支持基于Agent的场景、动态对象操作和多样化的交互类型。该系统设计易于使用和快速迭代，能够生成适合原型设计Agent叙事的虚拟Agent活动。使用四种流行的轻量级LLM评估了所开发系统的性能。在多种复杂性场景下测量了每个模型的处理和响应时间。分析收集到的数据，以比较不同场景之间的一致性，并突出每个模型在程序化Agent叙事生成方面的相对效率和适用性。结果表明，LLM可以可靠地将高级场景描述转换为可执行的基于Agent的行为。

## 🔬 方法详解

**问题定义**：现有Agent叙事生成方法通常依赖于预定义的规则或有限的状态机，难以处理复杂的场景和多样化的交互。手动设计Agent行为繁琐且耗时，缺乏快速原型设计和迭代的能力。因此，需要一种能够根据场景描述自动生成Agent行为的系统，以提高叙事生成的效率和灵活性。

**核心思路**：利用大型语言模型（LLM）的自然语言理解和生成能力，将场景描述转化为Agent的行为序列。用户通过图形界面创建场景，系统将场景信息转化为自然语言提示，输入LLM，LLM生成结构化的行为描述，最后由解析器将行为描述转化为可执行的Agent动作。这种方法的核心在于利用LLM作为场景描述和Agent行为之间的桥梁，从而实现自动化的叙事生成。

**技术框架**：该系统主要包含以下几个模块：1) 场景编辑器：允许用户拖拽Agent和对象，并为其分配语义元数据。2) 场景描述生成器：将场景信息序列化为自然语言提示。3) LLM：接收场景描述，生成结构化的Agent行为描述。4) 行为解析器：解析LLM的输出，将其转化为可执行的Agent动作。5) Agent行为执行器：控制Agent的动画和交互。整个流程是从场景创建开始，经过LLM的推理和生成，最终实现Agent在虚拟环境中的行为。

**关键创新**：该方法最重要的创新点在于利用LLM作为Agent叙事生成的中心环节。与传统的基于规则或状态机的方法相比，LLM能够理解更复杂的场景描述，并生成更自然、更丰富的Agent行为。此外，该系统还支持动态对象操作和多样化的交互类型，进一步提高了叙事生成的灵活性和可扩展性。

**关键设计**：场景描述生成器的设计至关重要，需要将场景信息以清晰、简洁的方式呈现给LLM。行为解析器需要能够准确地解析LLM的输出，并将其转化为可执行的Agent动作。此外，选择合适的LLM也是关键，需要考虑模型的推理能力、生成速度和成本。论文中使用了四种轻量级LLM进行评估，并比较了它们在不同复杂性场景下的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20550v1/fig1-new.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20550v1/fig2a.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20550v1/fig2b.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该系统能够有效地将场景描述转化为可执行的Agent行为。论文评估了四种轻量级LLM的性能，并比较了它们在不同复杂性场景下的处理和响应时间。结果显示，LLM能够可靠地将高级场景描述转换为可执行的基于Agent的行为，为程序化叙事生成提供了新的思路。

## 🎯 应用场景

该研究成果可应用于游戏开发、虚拟现实、教育培训等领域。例如，游戏开发者可以利用该系统快速生成游戏角色的行为脚本，提高开发效率。在教育领域，可以创建交互式虚拟环境，让学生通过与虚拟Agent互动来学习知识。此外，该系统还可以用于电影制作、广告设计等领域，为创意人员提供更便捷的叙事生成工具。

## 📄 摘要（原文）

> This paper presents a system for procedurally generating agent-based narratives using large language models (LLMs). Users could drag and drop multiple agents and objects into a scene, with each entity automatically assigned semantic metadata describing its identity, role, and potential interactions. The scene structure is then serialized into a natural language prompt and sent to an LLM, which returns a structured string describing a sequence of actions and interactions among agents and objects. The returned string encodes who performed which actions, when, and how. A custom parser interprets this string and triggers coordinated agent behaviors, animations, and interaction modules. The system supports agent-based scenes, dynamic object manipulation, and diverse interaction types. Designed for ease of use and rapid iteration, the system enables the generation of virtual agent activity suitable for prototyping agent narratives. The performance of the developed system was evaluated using four popular lightweight LLMs. Each model's process and response time were measured under multiple complexity scenarios. The collected data were analyzed to compare consistency across the examined scenarios and to highlight the relative efficiency and suitability of each model for procedural agent-based narratives generation. The results demonstrate that LLMs can reliably translate high-level scene descriptions into executable agent-based behaviors.

