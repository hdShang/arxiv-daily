---
layout: default
title: VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety
---

# VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety

**arXiv**: [2510.18214v1](https://arxiv.org/abs/2510.18214) | [PDF](https://arxiv.org/pdf/2510.18214.pdf)

**作者**: Shruti Palaskar, Leon Gatys, Mona Abdelrahman, Mar Jacobo, Larry Lindsey, Rutika Moharir, Gunnar Lund, Yang Xu, Navid Shiee, Jeffrey Bigham, Charles Maalouf, Joseph Yitan Cheng

---

## 💡 一句话要点

**提出VLSU框架以评估多模态模型在联合图像-文本理解中的安全风险**

**关键词**: `多模态安全评估` `联合图像-文本理解` `安全模式分类` `基准数据集` `组合推理失败` `模型对齐差距`

## 📋 核心要点

1. 核心问题：现有安全评估忽略多模态联合解释风险，导致过阻断或欠拒绝有害内容
2. 方法要点：构建细粒度严重性分类和组合分析，覆盖17种安全模式的大规模基准
3. 实验或效果：模型在联合推理时准确率降至20-55%，34%错误源于组合推理缺失

## 📄 摘要（原文）

> Safety evaluation of multimodal foundation models often treats vision and
> language inputs separately, missing risks from joint interpretation where
> benign content becomes harmful in combination. Existing approaches also fail to
> distinguish clearly unsafe content from borderline cases, leading to
> problematic over-blocking or under-refusal of genuinely harmful content. We
> present Vision Language Safety Understanding (VLSU), a comprehensive framework
> to systematically evaluate multimodal safety through fine-grained severity
> classification and combinatorial analysis across 17 distinct safety patterns.
> Using a multi-stage pipeline with real-world images and human annotation, we
> construct a large-scale benchmark of 8,187 samples spanning 15 harm categories.
> Our evaluation of eleven state-of-the-art models reveals systematic joint
> understanding failures: while models achieve 90%-plus accuracy on clear
> unimodal safety signals, performance degrades substantially to 20-55% when
> joint image-text reasoning is required to determine the safety label. Most
> critically, 34% of errors in joint image-text safety classification occur
> despite correct classification of the individual modalities, further
> demonstrating absent compositional reasoning capabilities. Additionally, we
> find that models struggle to balance refusing unsafe content while still
> responding to borderline cases that deserve engagement. For example, we find
> that instruction framing can reduce the over-blocking rate on borderline
> content from 62.4% to 10.4% in Gemini-1.5, but only at the cost of
> under-refusing on unsafe content with refusal rate dropping from 90.8% to
> 53.9%. Overall, our framework exposes weaknesses in joint image-text
> understanding and alignment gaps in current models, and provides a critical
> test bed to enable the next milestones in research on robust vision-language
> safety.

