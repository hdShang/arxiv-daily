---
layout: default
title: Disc3D: Automatic Curation of High-Quality 3D Dialog Data via Discriminative Object Referring
---

# Disc3D: Automatic Curation of High-Quality 3D Dialog Data via Discriminative Object Referring

**arXiv**: [2511.18817v1](https://arxiv.org/abs/2511.18817) | [PDF](https://arxiv.org/pdf/2511.18817.pdf)

**作者**: Siyuan Wei, Chunjie Wang, Xiao Liu, Xiaosheng Yan, Zhishan Zhou, Rui Huang

---

## 💡 一句话要点

**提出Disc3D自动管道以解决3D多模态大模型数据稀缺与歧义问题**

**关键词**: `3D多模态大模型` `自动数据生成` `对象指代消歧` `场景图构建` `多任务对话合成` `大规模数据集`

## 📋 核心要点

1. 核心问题：3D多模态大模型因高质量对话数据稀缺和视角、对象指代歧义而落后于2D模型
2. 方法要点：结合规则约束与2D MLLMs/LLMs，自动生成无歧义、高质量3D场景对话数据
3. 实验或效果：在公共基准和Disc3D-QA任务上训练模型，实现一致显著性能提升

## 📄 摘要（原文）

> 3D Multi-modal Large Language Models (MLLMs) still lag behind their 2D peers, largely because large-scale, high-quality 3D scene-dialogue datasets remain scarce. Prior efforts hinge on expensive human annotation and leave two key ambiguities unresolved: viewpoint ambiguity, where spatial language presumes unknown camera poses, and object referring ambiguity, where non-exclusive descriptions blur the line between targets and distractors. We therefore present a fully automated pipeline that converts raw 3D scans into unambiguous, high-quality dialogue data at a fraction of the previous cost. By synergizing rule-based constraints with 2D MLLMs and LLMs, the pipeline enables controllable, scalable generation without human intervention. The pipeline comprises four stages: (1) meta-annotation collection harvesting object-, frame-, and scene-level captions, (2) scene graph construction with relation correction to capture proximal object relations, (3) discriminative object referring that generates exclusive and compact descriptions, and (4) multi-task data generation synthesizing diverse dialogues. Our pipeline systematically mitigates inherent flaws in source datasets and produces the final Disc3D dataset, over 2 million samples in 25K hybrid 3D scenes, spanning scene, view, and object captioning, visual grounding, and five object-centric QA tasks. Extensive experiments demonstrate that training with Disc3D yields consistent, significant improvements on both public benchmarks and our multifaceted Disc3D-QA tasks. Code, data, and models will be publicly available.

