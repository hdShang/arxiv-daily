---
layout: default
title: "LLM-RG: Referential Grounding in Outdoor Scenarios using Large Language Models"
---

# LLM-RG: Referential Grounding in Outdoor Scenarios using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25528" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25528v2</a>
  <a href="https://arxiv.org/pdf/2509.25528.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25528v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25528v2', 'LLM-RG: Referential Grounding in Outdoor Scenarios using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranav Saxena, Avigyan Bhattacharya, Ji Zhang, Wenshan Wang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-09-29 (更新: 2025-10-21)

**备注**: Human-aware Embodied AI Workshop @ IROS 2025

---

## 💡 一句话要点

**LLM-RG：利用大语言模型实现户外场景下的指称对象定位**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指称对象定位` `大型语言模型` `视觉语言模型` `户外场景` `自动驾驶`

## 📋 核心要点

1. 户外场景指称对象定位面临场景复杂、对象相似等挑战，现有方法难以有效解析自然语言指称。
2. LLM-RG结合VLM提取视觉特征，利用LLM进行符号推理，将视觉信息和空间信息融入自然语言提示。
3. 在Talk2Car数据集上，LLM-RG显著优于LLM和VLM基线，3D空间线索的加入进一步提升了性能。

## 📝 摘要（中文）

由于场景变化大、视觉相似对象多以及动态元素复杂化了自然语言指称的解析（例如，“右边的黑色汽车”），户外驾驶场景中的指称对象定位具有挑战性。我们提出了LLM-RG，一种混合管道，它结合了现成的视觉-语言模型进行细粒度属性提取，以及大型语言模型进行符号推理。LLM-RG处理图像和自由形式的指称表达式，首先使用LLM提取相关的对象类型和属性，然后检测候选区域，使用VLM生成丰富的视觉描述符，并将这些描述符与空间元数据组合成自然语言提示，输入到LLM中进行思维链推理，以识别指称对象的边界框。在Talk2Car基准测试中，LLM-RG相对于基于LLM和VLM的基线都取得了显著的提升。此外，我们的消融实验表明，添加3D空间线索可以进一步改善定位效果。我们的结果证明了VLM和LLM的互补优势，以零样本方式应用于鲁棒的户外指称对象定位。

## 🔬 方法详解

**问题定义**：论文旨在解决户外驾驶场景中，根据自然语言描述精确定位特定对象的问题。现有方法难以有效处理复杂场景、视觉相似对象以及动态环境带来的挑战，导致指称对象定位的准确率较低。

**核心思路**：论文的核心思路是结合视觉-语言模型（VLM）和大型语言模型（LLM）的优势。VLM擅长提取细粒度的视觉特征，而LLM擅长进行符号推理和自然语言理解。通过将两者结合，可以更有效地解析自然语言指称，并将其与视觉信息关联起来。

**技术框架**：LLM-RG的整体架构包含以下几个主要模块：1) 使用LLM提取对象类型和属性；2) 检测候选区域；3) 使用VLM生成视觉描述符；4) 将视觉描述符和空间元数据组合成自然语言提示；5) 使用LLM进行思维链推理，最终确定指称对象的边界框。

**关键创新**：该方法最重要的创新点在于将VLM和LLM以一种互补的方式结合起来，利用VLM提取视觉特征，并利用LLM进行推理和决策。此外，该方法还考虑了3D空间信息，进一步提升了定位的准确性。

**关键设计**：该方法的关键设计包括：1) 使用预训练的VLM和LLM，无需额外的训练数据；2) 将视觉描述符和空间元数据以自然语言的形式输入到LLM中，方便LLM进行推理；3) 使用思维链推理，逐步缩小搜索范围，最终确定指称对象。

## 📊 实验亮点

LLM-RG在Talk2Car基准测试中取得了显著的性能提升，超过了基于LLM和VLM的基线方法。消融实验表明，添加3D空间线索可以进一步提高定位精度。这些结果验证了VLM和LLM结合的有效性，以及3D空间信息的重要性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能监控等领域。例如，在自动驾驶中，可以利用该技术理解驾驶员或乘客的指令，从而实现更智能的人机交互。在机器人导航中，可以帮助机器人理解自然语言指令，从而更好地完成任务。在智能监控中，可以根据自然语言描述快速定位目标对象。

## 📄 摘要（原文）

> Referential grounding in outdoor driving scenes is challenging due to large scene variability, many visually similar objects, and dynamic elements that complicate resolving natural-language references (e.g., "the black car on the right"). We propose LLM-RG, a hybrid pipeline that combines off-the-shelf vision-language models for fine-grained attribute extraction with large language models for symbolic reasoning. LLM-RG processes an image and a free-form referring expression by using an LLM to extract relevant object types and attributes, detecting candidate regions, generating rich visual descriptors with a VLM, and then combining these descriptors with spatial metadata into natural-language prompts that are input to an LLM for chain-of-thought reasoning to identify the referent's bounding box. Evaluated on the Talk2Car benchmark, LLM-RG yields substantial gains over both LLM and VLM-based baselines. Additionally, our ablations show that adding 3D spatial cues further improves grounding. Our results demonstrate the complementary strengths of VLMs and LLMs, applied in a zero-shot manner, for robust outdoor referential grounding.

