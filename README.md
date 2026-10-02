# Innovation Competition Skill

面向中国高校创新创业类竞赛的 Codex Skill，适用于大创、挑战杯、中国国际大学生创新大赛、创青春等场景。

它以官方规则和可核验证据为基础，统一组织商业计划书、路演 PPT、财务预测、海报、答辩问答与佐证材料，避免不同交付物之间的数据和表述冲突。当前版本还提供分阶段门控、评委红队测试和可初始化的项目工作区。

## 主要能力

- 核对赛道、资格、截止时间、模板和评分标准
- 建立主张—证据台账，区分已验证事实、用户陈述、预测和证据缺口
- 将项目材料映射到评分项，识别硬性阻断项
- 区分 Intake、Audit、Strategy、Build、Defense 和 Final QC 六种模式
- 一键生成竞赛简报、证据台账、评分矩阵、答辩题库和提交门控模板
- 协同 PPT、文档、表格、海报、市场分析和科研绘图类 Skill
- 执行跨文件一致性、渲染、权限、版本冻结和提交前真实性检查

## 安装

将仓库克隆到 Codex Skills 目录：

```bash
git clone https://github.com/Z-lab-boop/innovation-competition-skill.git ~/.codex/skills/innovation-competition
```

重新启动或刷新 Codex 后，即可通过 `$innovation-competition` 明确调用；在匹配的竞赛材料任务中也允许自动触发。

## 初始化竞赛工作区

```bash
python3 ~/.codex/skills/innovation-competition/scripts/init_competition_workspace.py ./my-competition-project
```

初始化器不会覆盖已有文件。

## 使用示例

```text
Use $innovation-competition to audit my Challenge Cup business plan,
map every claim to evidence, and identify submission blockers.
```

```text
使用 $innovation-competition，根据本届官方评分标准审查我的路演 PPT，
按严重程度列出问题，并生成证据补齐和答辩训练清单。
```

## 真实性边界

本 Skill 不会虚构或夸大专利、软著、论文、奖项、用户、合同、营收、测试结果、市场数据或团队履历。预测值必须标注假设、情景、来源和日期。

## 许可证

当前仓库未附加开源许可证。公开可见不等于自动授予复制、修改或再分发权利。
